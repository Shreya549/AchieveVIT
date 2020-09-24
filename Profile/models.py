from django.db import models
from Accounts.models import Faculty, HR
# Create your models here.

class FacultyProfile(models.Model):
    empid = models.CharField(primary_key=True, db_index = True)
    owner = models.ForeignKey(
        Faculty, on_delete=models.CASCADE, related_name='faculty', unique=True)
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    post = models.CharField(max_length = 100)
    school = models.CharField(max_length = 100)

class HRProfile(models.Model):
    empid = models.CharField(primary_key=True, db_index = True)
    owner = models.ForeignKey(
        HR, on_delete=models.CASCADE, related_name='hr', unique=True)
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    post = models.CharField(max_length = 100)
