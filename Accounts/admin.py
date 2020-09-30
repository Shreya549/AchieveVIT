from django.contrib import admin
from .models import User, Faculty, HR, OTPStore

admin.site.register(User)
admin.site.register(Faculty)
admin.site.register(HR)
admin.site.register(OTPStore)