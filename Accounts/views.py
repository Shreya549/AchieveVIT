from django.conf import settings
import jwt, requests, uuid
from .models import User, Faculty, HR
from rest_framework.views import APIView
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from rest_framework import status, serializers
from rest_framework import viewsets, permissions, generics
from .serializers import FacultyRegistrationSerializer, HRRegistrationSerializer
from .serializers import UserLoginSerializer
import uuid, os, base64, environ
from django.utils.crypto import get_random_string
from django.dispatch import receiver
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from datetime import datetime, timezone

# Create your views here.
class FacultyRegistration(APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = FacultyRegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        try:
            serializer.is_valid()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except:
            return Response({"error" : "Employee Id already exists"}, status = 403)  


class HRRegistration(APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = HRRegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        try:
            serializer.is_valid()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except:
            return Response({"error" : "Employee ID already exists"}, status = 403)  


class UserLogin(APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserLoginSerializer

    def post(self, request):

        serializer = self.serializer_class(data=request.data)

        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
