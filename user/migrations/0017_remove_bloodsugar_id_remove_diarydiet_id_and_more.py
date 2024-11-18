# Generated by Django 5.1.1 on 2024-09-20 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0016_alter_bloodpressure_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bloodsugar',
            name='id',
        ),
        migrations.RemoveField(
            model_name='diarydiet',
            name='id',
        ),
        migrations.RemoveField(
            model_name='weight',
            name='id',
        ),
        migrations.DeleteModel(
            name='BloodPressure',
        ),
        migrations.DeleteModel(
            name='BloodSugar',
        ),
        migrations.DeleteModel(
            name='DiaryDiet',
        ),
        migrations.DeleteModel(
            name='Weight',
        ),
    ]