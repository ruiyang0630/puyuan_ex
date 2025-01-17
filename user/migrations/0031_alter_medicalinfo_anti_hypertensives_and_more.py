# Generated by Django 5.1.1 on 2024-09-28 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0030_alter_default_bmi_max_alter_default_bmi_min_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicalinfo',
            name='anti_hypertensives',
            field=models.BooleanField(default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='medicalinfo',
            name='diabetes_type',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='medicalinfo',
            name='insulin',
            field=models.BooleanField(default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='medicalinfo',
            name='oad',
            field=models.BooleanField(default=0.0, null=True),
        ),
    ]
