from django.urls import path, include
from rest_framework.response import Response
from rest_framework.routers import DefaultRouter
from .views import FacultyRegistration, HRRegistration, UserLogin, OTPCheckView, OTPVerification

urlpatterns = [
    path('register-faculty/', FacultyRegistration.as_view()),
    path('register-hr/', HRRegistration.as_view()),
    path('login/', UserLogin.as_view()),
    path('verifyOTP', OTPVerification.as_view()),
    path('checkOTP', OTPCheckView.as_view())
]