from django.shortcuts import render
from rest_framework import generics, status
from .serializers import PatientSerializer, ClinicSerializer, AppointmentSerializer, CreatePatientSerializer, CreateClinicSerializer, CreateAppointmentSerializer
from .models import Patient, Clinic, Appointment
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from datetime import date
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from twilio.twiml.messaging_response import MessagingResponse

# Create your views here.


class PatientView(generics.CreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class ClinicView(generics.CreateAPIView):
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer

    def get(self, request, format=None):
        clinics = Clinic.objects.all()
        serializer = ClinicSerializer(clinics, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AppointmentView(generics.CreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def get(self, request, format=None):
        appointments = Appointment.objects.all()
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


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

    # new stuff
    # authentication_classes = [TokenAuthentication, ]
    # permission_classes = [IsAuthenticated, ]

    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            time = serializer.data.get('time')
            clinic = serializer.data.get('clinic')
            # clinic = self.request.session.session_key
            appointment = Appointment(time=time, clinic=clinic)
            appointment.save()
            appointment.fillAppointment()
            return Response(AppointmentSerializer(appointment).data, status=status.HTTP_201_CREATED)
        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)
        # i think we need this to identify the clinic, might have something to do with the user thing tho


class LoginClinicView(APIView):
    serializer_class = CreateAppointmentSerializer


class GetAppointment(APIView):
    serializer_class = AppointmentSerializer
    lookup_url_kwarg = 'clinic'

    def get(self, request, Format=None):
        clinic = self.request.session.session_key
        if clinic != None:
            appointment = Appointment.objects.filter(
                clinic=clinic, date=date.today())
            if len(appointment) > 0:
                data
                for i in range(len(appointment)):
                    data.append(AppointmentSerializer(appointment[i]).data)
                return data

@csrf_exempt
class Reply(APIView):    
    def reply(request):
        request_body = request.POST.get('Body')
        from_number = request.POST.get('From', '')

        p = api.models.Patient.objects.filter(phoneNumber=from_number)
        a = api.models.Appointment.objects.filter(patient=p)
        if request_body =='YES':
            a.confirmAppointment()
        if request_body =='NO':
            a.cancelAppointment()

        return HttpResponse(str(response))

