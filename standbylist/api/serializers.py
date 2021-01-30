from rest_framework import serializers
from .models import Patient

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('id', 'age', 'firstName', 'lastName', 'phoneNumber', 'email', 'vaccinationStatus', 'notificationStatus', 
            'occupation', 'transport', 'highRiskHousehold', 'healthcareNum', 'clinic')
