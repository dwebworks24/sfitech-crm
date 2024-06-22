from django.urls import path
from apps.authentication import views

urlpatterns = [
    path('', views.otp_login, name='home'),
    path('register/', views.register, name='register'),
    path('sigin/', views.sigin, name='sigin'),
    
]