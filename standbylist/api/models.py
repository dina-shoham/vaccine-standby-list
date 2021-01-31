from django.db import models
from geopy.distance import geodesic
from celery.schedules import crontab
from celery.task import periodic_task
import datetime
from twilio.rest import Client



class Patient(models.Model):
    NODOSE = '0D'
    ONEDOSE = '1D'
    TWODOSE = '2D'
    VACCINATION_STATUS = (
        (NODOSE, 'No doses'),
        (ONEDOSE, 'One dose'),
        (TWODOSE, 'Two doses'),
    )

    UNNOTIFIED = 'Unnotified'
    NOTIFIED = 'Notified'
    CONFIRMED = 'Confirmed'
    DECLINED = 'Declined'
    TIMEOUT = 'Timed out'
    VACCINATED = 'Vaccinated'
    NOTIFICATION_STATUS = (
        (UNNOTIFIED, 'Unnotified'),
        (NOTIFIED, 'Notified'),
        (CONFIRMED, 'Confirmed'),
        (DECLINED, 'Declined'),
        (TIMEOUT, 'Timed out'),
        (VACCINATED, 'Vaccinated'),
    )

    TIERONE = 'Tier 1'
    TIERTWO = 'Tier 2'
    TIERTHREE = 'Tier 3'
    TIERFOUR = 'Tier 4'
    OCCUPATION = (
        (TIERONE, 'Tier 1'),
        (TIERTWO, 'Tier 2'),
        (TIERTHREE, 'Tier 3'),
        (TIERFOUR, 'Tier 4'),
    )

    CAR = 'Car'
    PUBLICTRANSIT = 'Public transit'
    WALK = 'Walk'
    BIKE = 'Bike'
    OTHER = 'Other'
    MODE_OF_TRANSIT = (
        (CAR, 'Car'),
        (PUBLICTRANSIT, 'Public transit'),
        (WALK, 'Walk'),
        (BIKE, 'Bike'),
        (OTHER, 'Other'),
    )
    age = models.PositiveIntegerField()
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    phoneNumber = models.CharField(max_length=10, unique=True)
    email = models.CharField(max_length=255)
    vaccinationStatus = models.CharField(
        max_length=2, choices=VACCINATION_STATUS, default=NODOSE)
    notificationStatus = models.CharField(max_length=255,
                                          choices=NOTIFICATION_STATUS, default=UNNOTIFIED)
    occupation = models.CharField(max_length=255, choices=OCCUPATION)
    transport = models.CharField(max_length=255, choices=MODE_OF_TRANSIT)
    highRiskHousehold = models.BooleanField()
    healthcareNum = models.CharField(max_length=255, unique=True)
    lat = models.FloatField("latitude", null=True)
    lon = models.FloatField("longitude", null=True)
    riskFactors = models.IntegerField(default=0)


class Clinic(models.Model):
    lat = models.FloatField("latitude", null=True)
    lon = models.FloatField("longitude", null=True)
    name = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255, null=True)

    # queue of patients will be found using get all patient by clinic in prioritization algorithm
    # when a clinic enters an appointment, it will create a new appointment

    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    OPEN = 'open'
    CONFIRMED = 'confirmed'
    FINISHED = 'finished'
    MISSED = 'missed'
    STATUS = (
        (OPEN, 'Open'),
        (CONFIRMED, 'Confirmed'),
        (FINISHED, 'Finished'),
        (MISSED, 'missed'),
    )
    # one to one to patient
    patient = models.OneToOneField(
        Patient, on_delete=models.DO_NOTHING, null=True)
    status = models.CharField(max_length=255, choices=STATUS, default=OPEN)
    clinic = models.CharField(max_length=255, null=True)
    # clinic = models.ForeignKey(
    #     'Clinic',
    #     on_delete=models.CASCADE,  # had to add this line also to fix an error -d
    #     default=''
    # )  # changed it to cascade i think it makes more sense
    time = models.TimeField(null=True)
    confirmationTime = models.TimeField(null=True)
    messageSentTime = models.TimeField(null=True)
    date = models.DateField(auto_now_add=True)

    def fillAppointment(self):  # able to be called
        p = self.findPatient()
        self.patient = p
        self.messageSentTime = datetime.datetime.now()
        self.save(update_fields=['messageSentTime', 'patient'])
        p.notificationStatus = 'Notified'
        p.save(update_fields=['notificationStatus'])
        # TO ADD send alert to twilio
        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        message = "Can you make it to a vaccination appointment today at " + \
            self.time + "? Reply YES or NO"
        sent = client.messages.create(
            body=message, to='+1'+self.patient.phoneNumber, from_='+12159774582')
        print(sent.sid)

    def confirmAppointment(self):  # STILL NEEDS TO BE CALLED
        self.status = 'confirmed'
        self.confirmationTime = datetime.datetime.now()
        self.save(update_fields=['confirmationTime', 'status'])
        self.patient.notificationStatus = 'Confirmed'
        self.patient.save(update_fields=['notificationStatus'])

    def finishAppointment(self):  # STILL NEEDS TO BE CALLED
        if self.patient.vaccinationStatus == '0D':
            self.patient.vaccinationStatus = '1D'
        elif self.patient.vaccinationStatus == '1D':
            self.patient.vaccinationStatus = '2D'
        self.status = "Finished"
        self.save(update_fields=['status'])
        self.patient.notificationStatus = 'Vaccinated'
        self.patient.save(update_fields=['vaccinationStatus'])

    def checkAppointment(self):
        if self.status == 'open':  # if theyve gotten the msg but havent responded in 30mins
            timeSinceSent = (datetime.datetime.now() -
                             self.messageSentTime).total_seconds()
            if timeSinceSent > 1800:
                fillAppointment()
                # TO ADD send msg that theyve been cancelled

        if self.status == "confirmed":  # if theyve confirmed but its 15mins past the appointment time
            timeSinceAppointment = (
                datetime.datetime.now()-self.time).total_seconds()
            if timeSinceAppointment > 900:
                self.status = "Missed"
                self.save(update_fields=['status'])

    def findPatient(self):
        # grabs list of patients who have less than 2 doses
        patients = Patient.objects.filter(notificationStatus="Unnotified")
        # Patient.vaccinationStatus != "2D",  # and who are unnotified
        # patientClinicDist(self.clinic.lat, self.clinic.lon, lat, lon) < 15)  # and who are within range

        curPatient = patients[0]
        curHighestRisk = 0
        for p in patients:
            if p.occupation == "Tier 1":
                tier = 1
            elif p.occupation == "Tier 2":
                tier = 2
            elif p.occupation == "Tier 3":
                tier = 3
            elif p.occupation == "Tier 4":
                tier = 4

            if p.highRiskHousehold == True:
                house = 1.1
            else:
                house = 1

            if p.vaccinationStatus == "0D":
                status = 1
            elif p.vaccinationStatus == "1D":
                status = 2.5

            risk = (p.riskFactors+1)*p.age*(5-tier)*house*status
            if(curHighestRisk < risk):
                curHighestRisk = risk
                curPatient = p

        return curPatient

# Daily reset of appointments


@periodic_task(run_every=crontab(hour=4, minute=20))
def dailyReset():
    patients = Patient.objects.all()
    for p in patients:
        p.notificationStatus = 'Unnotified'
        p.save(update_fields=['notificationStatus'])
        # remove all appointments

# every 10 mins, updates all appointment statuses


@periodic_task(run_every=crontab(minute='*/10'))
def updateAppointments():
    appointments = Appointment.objects.all()
    for a in appointments:
        a.checkAppointment()


def patientClinicDist(patientLat, patientLon, clinicLat, clinicLon):
    patient = (patientLat, patientLon)
    clinic = (clinicLat, clinicLon)
    return (geodesic(patient, clinic).km)
