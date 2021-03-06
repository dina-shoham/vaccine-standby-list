from django.urls import path
from .views import PatientView
from .views import CreatePatientView
from .views import ClinicView
from .views import CreateClinicView
from .views import LoginClinicView
from .views import AppointmentView
from .views import CreateAppointmentView
from .views import Reply

urlpatterns = [
    path('patient', PatientView.as_view()),
    path('create-patient', CreatePatientView.as_view()),
    path('clinic', ClinicView.as_view()),
    path('create-clinic', CreateClinicView.as_view()),
    path('login-clinic', LoginClinicView.as_view()),
    path('appointment', AppointmentView.as_view()),
    path('create-appointment', CreateAppointmentView.as_view()),
    path('', Reply)
]
