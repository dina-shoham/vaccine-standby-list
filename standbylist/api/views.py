from django.shortcuts import render
from rest_framework import generics
from .serializers import PatientSerializer
from .serializers import ClinicSerializer
from .serializers import AppointmentSerializer
from .models import Patient
from .models import Clinic
from .models import Appointment

# Create your views here.

class PatientView(generics.CreateAPIView):
    queryset = Patient.objects.all()
    serializer_class=PatientSerializer

class ClinicView(generics.CreateAPIView):
    queryset = Clinic.objects.all()
    serializer_class=ClinicSerializer

class AppointmentView(generics.CreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class=AppointmentSerializer