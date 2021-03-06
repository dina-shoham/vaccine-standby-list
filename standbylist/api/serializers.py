from rest_framework import serializers
from .models import Patient
from .models import Clinic
from .models import Appointment


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('id', 'age', 'firstName', 'lastName', 'phoneNumber', 'email', 'vaccinationStatus',
                  'occupation', 'transport', 'highRiskHousehold', 'healthcareNum', 'riskFactors')


class ClinicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinic
        fields = ('id', 'lat', 'lon', 'name', 'username', 'password')


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ('id', 'patient', 'status', 'clinic', 'time', 'date')


# create serializers
class CreatePatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('age', 'firstName', 'lastName', 'phoneNumber', 'email', 'vaccinationStatus',
                  'occupation', 'transport', 'highRiskHousehold', 'healthcareNum', 'lat', 'lon', 'riskFactors')


class CreateClinicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinic
        fields = ('name', 'email', 'address',
                  'username', 'password', 'lat', 'lon')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}


class CreateAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ('time', 'clinic')

# will need a serializer for validating clinic logins
