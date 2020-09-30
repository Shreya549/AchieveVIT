from django.conf import settings
import jwt, requests, uuid
from .models import User, Faculty, HR
from rest_framework.views import APIView
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from rest_framework import status, serializers
from rest_framework import viewsets, permissions, generics
from .serializers import FacultyRegistrationSerializer, HRRegistrationSerializer, ChangePasswordSerializer
from .serializers import UserLoginSerializer
import uuid, os, base64, environ
from django.utils.crypto import get_random_string
from django.dispatch import receiver
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from datetime import datetime, timezone
from .models import OTPStore
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)   
)
environ.Env.read_env()

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "try.settings.local")
SENDGRID_API_KEY = env('SENDGRID_API_KEY')

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

class OTPVerification(APIView):

    def post(self, request):

        sendto_email = request.data["email"]
        otp = uuid.uuid4().hex[:6].upper()
        subject = "Achieve Verification OTP"
        message = "OTP for password change -<h1>" + otp + "</h1>"
        
        otp = OTPStore.objects.create(
                email = sendto_email,
                otp = otp,
                timestamp = datetime.now(timezone.utc)
            )
        otp.save()
        
        msg = message
        message = Mail(
            from_email='shreya.chatterjee2018@vitstudent.ac.in',
            to_emails=sendto_email,
            subject=subject,
            html_content=msg)
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        return Response(status = response.status_code)

class OTPCheckView(APIView):
    def post(self, request):
        email = request.data['email'] 
        otp = request.data['otp']
        query = OTPStore.objects.filter(email = email, otp = otp).order_by('-timestamp')
        if (query.exists()):
            timestamp = query.values_list('timestamp', flat=True)[0]
            duration = datetime.now(timezone.utc) - timestamp
            duration_in_s = duration.total_seconds()
            minutes = divmod(duration_in_s, 60)[0]
            if (minutes<=5):
                return Response({"message" : "OTP Verified"}, status = 200)
            else:
                return Response({"message" : "Time Out"}, status = 400)

        else:
            return Response({"message" : "OTP does not exist"}, status = 404)

class ChangePasswordView(UpdateAPIView):
        """
        An endpoint for changing password.
        """
        serializer_class = ChangePasswordSerializer
        model = User
        permission_classes = [permissions.IsAuthenticated]

        def get_object(self, queryset=None):
            obj = self.request.user
            return obj

        def update(self, request, *args, **kwargs):
            self.object = self.get_object()
            serializer = self.get_serializer(data=request.data)

            if serializer.is_valid():
                # Check old password
                if not self.object.check_password(serializer.data.get("old_password")):
                    return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
                # set_password also hashes the password that the user will get
                self.object.set_password(serializer.data.get("new_password"))
                self.object.save()
                response = {
                    'status': 'success',
                    'code': status.HTTP_200_OK,
                    'message': 'Password updated successfully',
                    'data': []
                }

                return Response(response)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



