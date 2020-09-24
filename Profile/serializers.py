from rest_framework import serializers
from .models import HRProfile, FacultyProfile

class FacultyProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacultyProfile
        fields = '__all__'
        read_only_fields = ('owner',)


class HRProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = HRProfile
        fields = '__all__'
        read_only_fields = ('owner',)