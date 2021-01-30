from django.shortcuts import render
from rest_framework import generics
from .serializers import PatientSerializer
from .models import Patient

# Create your views here.

class PatientView(generics.CreateAPIView):
    queryset = Patient.objects.all()
    serializer_class=PatientSerializer
