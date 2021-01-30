from django.db import models

# Create your models here.
class Patient(models.Model):
    NODOSE='0D'
    ONEDOSE='1D'
    TWODOSE='2D'
    VACCINATION_STATUS=(
        (NODOSE, 'No doses'),
        (ONEDOSE, 'One dose'),
        (TWODOSE, 'Two doses'),
    )

    UNNOTIFIED='Unnotified'
    NOTIFIED='Notified'
    CONFIRMED='Confirmed'
    DECLINED='Declined'
    TIMEOUT='Timed out'
    VACCINATED='Vaccinated'
    NOTIFICATION_STATUS=(
        (UNNOTIFIED, 'Unnotified'),
        (NOTIFIED, 'Notified'),
        (CONFIRMED, 'Confirmed'),
        (DECLINED, 'Declined'),
        (TIMEOUT, 'Timed out'),
        (VACCINATED, 'Vaccinated'),
    )

    TIERONE='Tier 1'
    TIERTWO='Tier 2'
    TIERTHREE='Tier 3'
    TIERFOUR='Tier 4'
    OCCUPATION=(
        (TIERONE, 'Tier 1'), 
        (TIERTWO, 'Tier 2'),
        (TIERTHREE, 'Tier 3'),
        (TIERFOUR, 'Tier 4'),
    )

    CAR='Car'
    PUBLICTRANSIT='Public transit'
    WALK='Walk'
    BIKE='Bike'
    OTHER='Other'
    MODE_OF_TRANSIT=(
        (CAR, 'Car'),
        (PUBLICTRANSIT, 'Public transit'),
        (WALK, 'Walk'),
        (BIKE, 'Bike'),
        (OTHER, 'Other'),
    )

    age = models.PositiveIntegerField()
    firstName = models.CharField()
    lastName = models.CharField()
    phoneNumber = models.CharField(max_length=10)
    email = models.CharField()
    #how do we do home address???
    #homeAddress
    vaccinationStatus = models.CharField(max_length=2, choices=VACCINATION_STATUS, default=NODOSE)
    notificationStatus = models.CharField(choices=NOTIFICATION_STATUS, default=UNNOTIFIED)
    occupation = models.CharField(choices=OCCUPATION)
    transport = models.CharField(choices=MODE_OF_TRANSIT)
    highRiskHousehold = models.BooleanField()
    healthcareNum = models.CharField(unique=True)
    #can an attribute be an object we create? 
    #enum Clinic home clinic