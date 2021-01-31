from django.shortcuts import render
from rest_framework import generics, status
from .serializers import PatientSerializer, ClinicSerializer, AppointmentSerializer, CreatePatientSerializer, CreateClinicSerializer, CreateAppointmentSerializer
from .models import Patient, Clinic, Appointment
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class PatientView(generics.CreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class ClinicView(generics.CreateAPIView):
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer


class AppointmentView(generics.CreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


class CreatePatientView(APIView):
    serializer_class = CreatePatientSerializer

    def post(self, request, format=None):
        # if no active session, creates a session
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            age = serializer.data.get('age')
            firstName = serializer.data.get('firstName')
            lastName = serializer.data.get('lastName')
            phoneNumber = serializer.data.get('phoneNumber')
            email = serializer.data.get('email')
            vaccinationStatus = serializer.data.get('vaccinationStatus')
            occupation = serializer.data.get('occupation')
            transport = serializer.data.get('transport')
            highRiskHousehold = serializer.data.get('highRiskHousehold')
            healthcareNum = serializer.data.get('healthcareNum')
            riskFactors = serializer.data.get('riskFactors')
            lat = serializer.data.get('lat')
            lon = serializer.data.get('lon')

            patient = Patient(age=age,
                              firstName=firstName,
                              lastName=lastName,
                              phoneNumber=phoneNumber,
                              email=email,
                              vaccinationStatus=vaccinationStatus,
                              occupation=occupation,
                              transport=transport,
                              highRiskHousehold=highRiskHousehold,
                              healthcareNum=healthcareNum,
                              riskFactors=riskFactors,
                              lat=lat,
                              lon=lon)
            patient.save()
            return Response(PatientSerializer(patient).data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)


class CreateClinicView(APIView):
    serializer_class = CreateClinicSerializer

    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            email = serializer.data.get('email')
            address = serializer.data.get('address')
            username = serializer.data.get('username')
            password = serializer.data.get('password')
            lat = serializer.data.get('lat')
            lon = serializer.data.get('lon')
            clinic = Clinic(
                name=name,
                email=email,
                address=address,
                username=username,
                password=password,
                lat=lat,
                lon=lon
            )
            clinic.save()
            return Response(ClinicSerializer(clinic).data, status=status.HTTP_201_CREATED)
        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)


class CreateAppointmentView(APIView):
    serializer_class = CreateAppointmentSerializer

    #new stuff
    authentication_classes=[TokenAuthentication, ]
    permission_classes=[IsAuthenticated, ]

    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            time = serializer.data.get('time')
            clinic = self.request.session.session_key
            appointment = Appointment(time=time, clinic=clinic)
            appointment.save()
            return Response(AppointmentSerializer(appointment).data, status=status.HTTP_201_CREATED)
        return Response(AppointmentSerializer(appointment).data, status=status.HTTP_400_BAD_REQUEST)
        # i think we need this to identify the clinic, might have something to do with the user thing tho

