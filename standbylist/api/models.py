from django.db import models

# Create your models here.
class Patient(models.Model):
    age = models.PositiveIntegerField();
    firstName = models.CharField();
    lastName = models.CharField();
    phoneNumber = models.CharField(max_length=10);
    email = models.CharField();
    #how do we do home address???
    #homeAddress
    #how do we do enum?
    #enum vaccination status
    #enum notification status
    #enum occupation
    #enum mode of transport to clinic
    highRiskHousehold = models.BooleanField();
    healthcareNum = models.CharField(unique=True);
    #can an attribute be an object we create? 
    #Clinic home clinic