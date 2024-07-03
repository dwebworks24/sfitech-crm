from django.urls import path
from apps.authentication import views

urlpatterns = [
    path('', views.otp_login, name='home'),
    path('register/', views.register, name='register'),
    path('otp_validate/', views.otp_validate, name='otp_validate'),
    
    
]