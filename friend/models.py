from django.db import models
from accounts.models import UserAuth

class Friend(models.Model):
    userid = models.ForeignKey(UserAuth, on_delete=models.CASCADE)
    relationid = models.IntegerField(null=True)
    friend_type = models.IntegerField(null=True)
    status = models.IntegerField(null=True, default=0)
    read = models.BooleanField(null=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)