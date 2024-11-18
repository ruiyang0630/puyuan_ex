from django.db import models
from accounts.models import UserAuth

class Notification(models.Model):
    member_id = models.ForeignKey(UserAuth, on_delete=models.CASCADE)
    reply_id = models.IntegerField()
    message = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Share(models.Model):
    fid = models.CharField(max_length=50)
    data_type = models.IntegerField()
    relation_type = models.IntegerField()