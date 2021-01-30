from django.db import models
#from geo.py import geodesic

# Create your models here.


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
    name = models.CharField(max_length=255)

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
    STATUS = (
        (OPEN, 'Open'),
        (CONFIRMED, 'Confirmed'),
        (FINISHED, 'Finished'),
    )
    # one to one to patient
    patient = models.OneToOneField(
        Patient, on_delete=models.DO_NOTHING, null=True)
    status = models.CharField(max_length=255, choices=STATUS, default=OPEN)
    clinic = models.ForeignKey(
        'Clinic',
        on_delete=models.CASCADE  # had to add this line also to fix an error -d
    )  # changed it to cascade i think it makes more sense
    time = models.TimeField()
    date = models.DateField(auto_now_add=True)

    def fillAppointment():
        p = findPatient(self.clinic, 15)
        #send alert to twilio

        #on twilio recieved:
            self.patient = p
            #set time of appointment confirmation to current time


# ALBERTA = 'Alberta'
# BC = 'British Columbia'
# MANITOBA = 'Manitoba'
# NB = 'New Brunswick'
# NEWFL = 'Newfoundland and Labrador'
# NWT = 'Northwest Territories'
# NS = 'Nova Scotia'
# NUNAVUT = 'Nunavut'
# ONTARIO = 'Ontario'
# PEI = 'Prince Edward Island'
# QUEBEC = 'Quebec'
# SK = 'Saskatchewan'
# YUKON = 'Yukon'
# PROVINCE = (
#     (ALBERTA, 'Alberta'),
#     (BC, 'British Columbia'),
#     (MANITOBA, 'Manitoba'),
#     (NB, 'New Brunswick'),
#     (NEWFL, 'Newfoundland and Labrador'),
#     (NWT, 'Northwest Territories'),
#     (NS, 'Nova Scotia'),
#     (NUNAVUT, 'Nunavut'),
#     (ONTARIO, 'Ontario'),
#     (PEI, 'Prince Edward Island'),
#     (QUEBEC, 'Quebec'),
#     (SK, 'Saskatchewan'),
#     (YUKON, 'Yukon'),
# )
# province = models.CharField(max_length=255, choices=PROVINCE)


def findPatient(clinic, clinicRange):
    patients = Patient.objects.filter(vaccinationStatus != "2D",  # grabs list of patients who have less than 2 doses
                                      notificationStatus == "Unnotified",  # and who are unnotified
                                      patientClinicDist(clinic.lat, clinic.lon, lat, lon) < clinicRange)  # and who are within range

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


def patientClinicDist(patientLat, patientLon, clinicLat, clinicLon):
    patient = (patientLat, patientLon)
    clinic = (clinicLat, clinicLon)
    return (geodesic(patient, clinic).km)
