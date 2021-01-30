from rest_framework import serializers
from .models import Patient
from .models import Clinic
from .models import Appointment

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('id', 'age', 'firstName', 'lastName', 'phoneNumber', 'email', 'vaccinationStatus', 'notificationStatus', 
            'occupation', 'transport', 'highRiskHousehold', 'healthcareNum', 'clinic')

class ClinicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinic
        fields = ('id', 'lat', 'long', 'name', 'username', 'password')

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Appointment
        fields = ('id', 'status', 'clinic', 'time', 'date')