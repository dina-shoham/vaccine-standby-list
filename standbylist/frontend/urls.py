from django.urls import path
from .views import index
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', index),
    path('signup', index),
    path('clinic/signup', index),
    path('clinic/login', auth_views.LoginView.as_view(template_name='clinic/login.html'), name = 'login'),
    path('clinic/logout', auth_views.LogoutView.as_view(template_name='clinic/logout.html'), name = 'logout'),
    path('', index),
]
