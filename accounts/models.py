from django.db import models
from django.contrib.auth.models import AbstractUser

class UserAuth(AbstractUser):
    phone = models.CharField(max_length=50, unique=True, null=True, blank=True, default='null')
    email = models.EmailField(max_length=50, unique=True)
    code = models.CharField(max_length=50, default=None, null=True)
    verified = models.BooleanField(default=False)
    privacy_policy = models.BooleanField(default=False)
    must_change_password = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = ['email']