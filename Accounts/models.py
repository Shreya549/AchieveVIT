from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import ugettext_lazy as _

from datetime import timedelta
from datetime import datetime as dtime
from django.conf import settings
from uuid import uuid4

import jwt
import time
import uuid

class UserManager(BaseUserManager):
    def create_user(
            self, email, empid, name, password=None,
            commit=True):
        """
        Creates and saves a User with the given email, first name, last name
        and password.
        """
        if not email:
            raise ValueError(_('Users must have an email address'))
        if not name:
            raise ValueError(_('Users must have a name'))
        if not empid:
            raise ValueError(_('Users must have an Employee Id'))

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            empid=empid
        )

        user.set_password(password)
        if commit:
            user.save(using=self._db)
        return user

    def create_superuser(self, email, empid, name, password):
        """
        Creates and saves a superuser with the given email, first name,
        last name and password.
        """
        user = self.create_user(
            email,
            password=password,
            name=name,
            empid=empid,
            commit=False,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, email):
        return self.get(email=email)


class FacultyManager(BaseUserManager):

    def create_student(self, name, email, empid, password=None):
        if email is None:
            raise TypeError('Users must have an email address.')
        student = Faculty(name=name, empid=empid,
                          email=self.normalize_email(email),
                          )
        student.set_password(password)
        student.is_active = True
        student.save()
        return student


class HRManager(BaseUserManager):

    def create_school(self, empid, name, email, password=None):
        if email is None:
            raise TypeError('Users must have an email address.')
        school = HR(name=name,empid=empid,
                        email=self.normalize_email(email))
        school.set_password(password)
        school.is_active = True
        school.save()
        return school

class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=100)
    email = models.EmailField(db_index=True, unique=True)
    empid = models.CharField(max_length = 5, db_index=True, unique = True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'
        ),
    )

    USERNAME_FIELD = 'empid'
    REQUIRED_FIELDS = ['name', 'email', 'empid']

    objects = UserManager()

    @property
    def token(self):
        dt = dtime.now() + timedelta(days=2)
        token = jwt.encode({
            'id': self.id,
            'exp': int(time.mktime(dt.timetuple()))
        }, settings.SECRET_KEY, algorithm='HS256')
        return token.decode('utf-8')

    def natural_key(self):
        return (self.name)

    def __str__(self):
        return self.email


class Faculty(User, PermissionsMixin):

    USERNAME_FIELD = 'empid'
    REQUIRED_FIELDS = ['name', 'email', 'empid']

    objects = FacultyManager()

    def __str__(self):
        return self.name


class HR(User, PermissionsMixin):

    USERNAME_FIELD = 'empid'
    REQUIRED_FIELDS = ['name', 'email', 'empid']

    objects = HRManager()

    def __str__(self):
        return self.name

