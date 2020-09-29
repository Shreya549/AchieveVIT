from django.shortcuts import render
from rest_framework import viewsets, permissions, generics
from .serializers import EducationSerializer, WorkExperienceSerializer, AchievementsSerializer
from .models import Education, WorkExperience, Achievements

# Create your views here.
class EducationViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = EducationSerializer

    def get_queryset(self):
        profile = EducationSerializer.objects.get(owner = self.request.user)
        return profile

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

class WorkExperienceViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = WorkExperienceSerializer

    def get_queryset(self):
        profile = WorkExperience.objects.get(owner = self.request.user)
        return profile

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

class AchievementsViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AchievementsSerializer

    def get_queryset(self):
        profile = Achievements.objects.get(owner = self.request.user)
        return profile

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

class EducationRetrieveView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = EducationSerializer

    def get_queryset(self):
        fk = self.request.GET.get('uuid')
        query = Education.objects.get(owner = fk)
        return query

class WorkExperienceRetrieveView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = WorkExperienceSerializer

    def get_queryset(self):
        fk = self.request.GET.get('uuid')
        query = WorkExperience.objects.get(owner = fk)
        return query

class AchievementsRetrieveView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AchievementsSerializer

    def get_queryset(self):
        fk = self.request.GET.get('uuid')
        query = Achievements.objects.get(owner = fk)
        return query
       
    


