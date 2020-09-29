from django.shortcuts import render
from rest_framework import viewsets, permissions, generics
from .serializers import EducationSerializer, WorkExperienceSerializer, AchievementsSerializer
from .models import Education, WorkExperience, Achievements
from Feed.models import Feed
from Profile.models import FacultyProfile

# Create your views here.
class EducationViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = EducationSerializer

    def get_queryset(self):
        profile = EducationSerializer.objects.get(owner = self.request.user)
        return profile

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)

        feed = Feed.objects.create(
            fk = serializer.data['uuid'],
            type = 'Education'
        )
        feed.save()

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

        feed = Feed.objects.create(
            fk = serializer.data['uuid'],
            type = 'Experience'
        )
        feed.save()

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

        feed = Feed.objects.create(
            fk = serializer.data['uuid'],
            type = 'Achievements'
        )
        feed.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

class EducationRetrieveView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = EducationSerializer

    def get_queryset(self):
        fk = self.request.GET.get('empid')
        owner = FacultyProfile.objects.get(pk = fk).owner
        query = Education.objects.filter(owner = owner)
        return query

class WorkExperienceRetrieveView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = WorkExperienceSerializer

    def get_queryset(self):
        fk = self.request.GET.get('empid')
        owner = FacultyProfile.objects.get(pk = fk).owner
        query = WorkExperience.objects.filter(owner = owner)
        return query

class AchievementsRetrieveView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AchievementsSerializer

    def get_queryset(self):
        fk = self.request.GET.get('empid')
        owner = FacultyProfile.objects.get(pk = fk).owner
        query = Achievements.objects.filter(owner = owner)
        return query
       
    



