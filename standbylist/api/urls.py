from django.urls import path
from .views import PatientView
from .views import CreatePatientView
from .views import ClinicView
from .views import AppointmentView
from .views import CreatePatientView

urlpatterns = [
    path('patient', PatientView.as_view()),
    path('create-patient', CreatePatientView.as_view()),
    path('clinic', ClinicView.as_view()),
    path('appointment', AppointmentView.as_view()),
    path('create-patient', CreatePatientView.as_view())
]
