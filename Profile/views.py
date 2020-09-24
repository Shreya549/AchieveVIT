from django.shortcuts import render
from rest_framework import viewsets, permissions, generics
from .serializers import FacultyProfileSerializer, HRProfileSerializer
from .models import FacultyProfile, HRProfile

# Create your views here.
class FacultyProfileView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FacultyProfileSerializer

    def get_queryset(self):
        profile = FacultyProfile.objects.get(owner = self.request.user)
        return profile

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)


class HRProfileView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = HRProfileSerializer

    def get_queryset(self):
        profile = HRProfile.objects.get(owner = self.request.user)
        return profile

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)


        