from django.db import models
from Accounts.models import Faculty
from uuid import uuid4
import uuid

# Create your models here.
class Feed(models.Model):
    uuid = models.UUIDField(default = uuid.uuid4, primary_key = True)
    fk = models.UUIDField()
    type = models.CharField(max_length = 100)
    timestamp = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)

