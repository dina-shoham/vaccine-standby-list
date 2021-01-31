from django.urls import path
from .views import index
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', index),
    path('signup', index),
    path('clinic/signup', index),
    path('', index),
    path('clinic/login', index),
    path('create-appointment', index)

]
