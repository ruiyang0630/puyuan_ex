# Generated by Django 5.1.1 on 2024-09-21 13:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_userauth_email'),
        ('user', '0020_alter_hba1c_a1c'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalInfo',
            fields=[
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('oad', models.BooleanField(null=True)),
                ('insulin', models.BooleanField(null=True)),
                ('anti_hypertensives', models.BooleanField(null=True)),
                ('diabetes_type', models.IntegerField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
