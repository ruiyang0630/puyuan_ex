from rest_framework import serializers
from django.conf import settings
from django.core.mail import send_mail
from .models import UserAuth

class Register(serializers.ModelSerializer):
    class Meta:
        model = UserAuth
        fields = ['email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, data):
        user = UserAuth.objects.create_user(
            username=data['email'],
            email=data['email'],
            password=data['password']
        )
        return user

def send_email(email, context, option):
    if option == 'code':
        title = '普元信箱驗證'
        context = f'您的驗證碼是 {context}.'
    elif option == 'forget':
        title = '普元臨時密碼'
        context = f'您的臨時密碼是 {context}\n請盡快登入並更改密碼.'
    send_mail(title, context, settings.EMAIL_HOST_USER,[email])