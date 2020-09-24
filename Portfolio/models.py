from django.db import models
from Accounts.models import Faculty
from uuid import uuid4
import uuid
# Create your models here.

class Education(models.Model):
    uuid = models.UUIDField(default = uuid.uuid4, primary_key = True)
    owner = models.ForeignKey(Faculty,  on_delete=models.CASCADE, related_name='faculty_edu', unique=True)
    university = models.CharField(max_length = 100, null = True, blank = True)
    degree = models.CharField(max_length = 100, null = True, blank = True)
    start_year = models.DateField()
    end_year = models.DateField()

class WorkExperience(models.Model):
    uuid = models.UUIDField(default = uuid.uuid4, primary_key = True)
    owner = models.ForeignKey(Faculty,  on_delete=models.CASCADE, related_name='faculty_we', unique=True)
    position = models.CharField(max_length = 100, null = True, blank = True)
    comp_name = models.CharField(max_length = 100, null = True, blank = True)
    description = models.CharField(max_length = 300, null = True, blank = True)
    period = models.CharField(max_length = 100, null = True, blank = True)

class Achievements(models.Model):
    uuid = models.UUIDField(default = uuid.uuid4, primary_key = True)
    owner = models.ForeignKey(Faculty,  on_delete=models.CASCADE, related_name='faculty_ach', unique=True)
    details = models.CharField(max_length = 300)
