from django.test import TestCase
import datetime

import api

api.models.Patient.objects.all().delete()
api.models.Clinic.objects.all().delete()
api.models.Appointment.objects.all().delete()

q= p.filter(id=1)[0]

p1 = api.models.Patient(id =1, age = 80, firstName = "Harold", lastName = "Smith", 
             phoneNumber = "4039729857", email = "harold@mail.tv", 
             occupation = 'Tier 3', transport = 'Car', highRiskHousehold = True, 
             healthcareNum = "20357819854", lat = 20.15, lon = 23.13, riskFactors = 3)
p1.save()

p2 = api.models.Patient(id =2, age = 27, firstName = "lil", lastName = "marco", 
             phoneNumber = "24572457", email = "lilmarco@rocketmail.org", 
             occupation = 'Tier 3', transport = 'Car', highRiskHousehold = False, 
             healthcareNum = "15472345", lat = 40.15, lon = -25.13, riskFactors = 6)
p2.save()

p3 = api.models.Patient(id =3, age = 56, firstName = "obama", lastName = "obama?idk his last name", 
             phoneNumber = "53463456", email = "obama@usa.us", 
             occupation = 'Tier 4', transport = 'Car', highRiskHousehold = True, 
             healthcareNum = "234161353", lat = 70.15, lon = 53.13, riskFactors = 3)
p3.save()

c1 = api.models.Clinic(lat = 37.3, lon = -8.0, name = "main clinic", email = "healthcare@vaccine", address = "ur moms house")
c1.save()

a1 = api.models.Appointment(clinic = c1, time = datetime.datetime.now())
a1.save()

a1.fillAppointment()
