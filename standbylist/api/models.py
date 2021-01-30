from django.db import models

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

    # many to one
    clinic = models.ForeignKey(
        'Clinic',
        on_delete=models.DO_NOTHING  # added this line bc i was getting a typeError -dina
    )

    class Clinic(models.Model):
        lat = models.FloatField("latitude")
        lon = models.FloatField("longitude")
        name = models.CharField(max_length=255)

        # queue of patients
        # list of today's available appointments

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

        status = models.CharField(max_length=255, choices=STATUS, default=OPEN)
        clinic = models.ForeignKey(
            'Clinic',
            on_delete=models.CASCADE  # had to add this line also to fix an error -d
        )                               #changed it to cascade i think it makes more sense
        time = models.TimeField()
        date = models.DateField(auto_now_add=True)


class Address(models.Model):
    street = models.CharField("Street Address", max_length=100)
    city = models.CharField("City", max_length=30)
    postalCode = models.CharField("Postal Code", max_length=6)
    #country = models.CharField("Country", max_length=3, choices=ISO_3166_CODES)

    ALBERTA = 'Alberta'
    BC = 'British Columbia'
    MANITOBA = 'Manitoba'
    NB = 'New Brunswick'
    NEWFL = 'Newfoundland and Labrador'
    NWT = 'Northwest Territories'
    NS = 'Nova Scotia'
    NUNAVUT = 'Nunavut'
    ONTARIO = 'Ontario'
    PEI = 'Prince Edward Island'
    QUEBEC = 'Quebec'
    SK = 'Saskatchewan'
    YUKON = 'Yukon'
    PROVINCE = (
        (ALBERTA, 'Alberta'),
        (BC, 'British Columbia'),
        (MANITOBA, 'Manitoba'),
        (NB, 'New Brunswick'),
        (NEWFL, 'Newfoundland and Labrador'),
        (NWT, 'Northwest Territories'),
        (NS, 'Nova Scotia'),
        (NUNAVUT, 'Nunavut'),
        (ONTARIO, 'Ontario'),
        (PEI, 'Prince Edward Island'),
        (QUEBEC, 'Quebec'),
        (SK, 'Saskatchewan'),
        (YUKON, 'Yukon'),
    )
    province = models.CharField(max_length=255, choices=PROVINCE)

    lat = models.FloatField("latitude")
    lon = models.FloatField("longitude")
