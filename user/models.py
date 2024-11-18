from django.db import models
from accounts.models import UserAuth

class UserProfile(models.Model):
    id = models.OneToOneField(UserAuth, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=100, null=True, default='null')
    birthday = models.CharField(max_length=100, null=True, default='')
    height = models.FloatField(null=True, default=0.0)
    weight = models.FloatField(null=True, default=0.0)
    gender = models.BooleanField(null=True)
    address = models.CharField(max_length=100, null=True, default='null')
    inviteCode = models.CharField(max_length=10, null=True, default='null')
    badge = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Default(models.Model):
    id = models.OneToOneField(UserAuth, on_delete=models.CASCADE, primary_key=True)
    sugar_delta_max = models.IntegerField(null=True)
    sugar_delta_min = models.IntegerField(null=True)
    sugar_morning_max = models.IntegerField(null=True, default=0)
    sugar_morning_min = models.IntegerField(null=True, default=0)
    sugar_evening_max = models.IntegerField(null=True, default=0)
    sugar_evening_min = models.IntegerField(null=True, default=0)
    sugar_before_max = models.IntegerField(null=True, default=0)
    sugar_before_min = models.IntegerField(null=True, default=0)
    sugar_after_max = models.IntegerField(null=True, default=0)
    sugar_after_min = models.IntegerField(null=True, default=0)
    systolic_max = models.IntegerField(null=True, default=0)
    systolic_min = models.IntegerField(null=True, default=0)
    diastolic_max = models.IntegerField(null=True, default=0)
    diastolic_min = models.IntegerField(null=True, default=0)
    pulse_max = models.IntegerField(null=True, default=0)
    pulse_min = models.IntegerField(null=True, default=0)
    weight_max = models.IntegerField(null=True, default=0)
    weight_min = models.IntegerField(null=True, default=0)
    bmi_max = models.IntegerField(null=True, default=0)
    bmi_min = models.IntegerField(null=True, default=0)
    body_fat_max = models.IntegerField(null=True, default=0)
    body_fat_min = models.IntegerField(null=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Setting(models.Model):
    id = models.OneToOneField(UserAuth, on_delete=models.CASCADE, primary_key=True)
    after_recording = models.BooleanField(null=True)
    no_recording_for_a_day = models.BooleanField(null=True)
    over_max_or_under_min = models.BooleanField(null=True)
    after_meal = models.BooleanField(null=True)
    unit_of_sugar = models.BooleanField(null=True)
    unit_of_weight = models.BooleanField(null=True)
    unit_of_height = models.BooleanField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class BloodPressure(models.Model):
    user_id = models.ForeignKey(UserAuth, on_delete=models.CASCADE)
    systolic = models.FloatField(max_length=3, null=True)
    diastolic = models.FloatField(max_length=3, null=True)
    pulse = models.FloatField(max_length=3, null=True)
    recorded_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Weight(models.Model):
    user_id = models.ForeignKey(UserAuth, on_delete=models.CASCADE)
    weight = models.FloatField(max_length=3, null=True)
    body_fat = models.FloatField(max_length=3, null=True)
    bmi = models.FloatField(max_length=3, null=True)
    recorded_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class BloodSugar(models.Model):
    user_id = models.ForeignKey(UserAuth, on_delete=models.CASCADE)
    sugar = models.IntegerField(null=True)
    timeperiod = models.IntegerField(null=True)
    recorded_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class DiaryDiet(models.Model):
    user_id = models.ForeignKey(UserAuth, on_delete=models.CASCADE)
    description = models.IntegerField(null=True)
    meal = models.IntegerField(null=True)
    tag = models.CharField(max_length=100, null=True)
    image = models.IntegerField(null=True)
    lat = models.FloatField(null=True)
    lng = models.FloatField(null=True)
    recorded_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class HbA1c(models.Model):
    user_id = models.ForeignKey(UserAuth, on_delete=models.CASCADE)
    a1c = models.IntegerField(null=True)
    recorded_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class MedicalInfo(models.Model):
    id = models.OneToOneField(UserAuth, on_delete=models.CASCADE, primary_key=True)
    oad = models.BooleanField(null=True, default=0.0)
    insulin = models.BooleanField(null=True, default=0.0)
    anti_hypertensives = models.BooleanField(null=True, default=0.0)
    diabetes_type = models.IntegerField(null=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class DrugInfo(models.Model):
    user_id = models.ForeignKey(UserAuth, on_delete=models.CASCADE)
    drugname = models.CharField(max_length=100, null=True)
    drug_type = models.BooleanField(null=True)
    recorded_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class UserCare(models.Model):
    user_id = models.ForeignKey(UserAuth, on_delete=models.CASCADE)
    member_id = models.IntegerField(null=True, default=0)
    reply_id = models.IntegerField(null=True, default=0)
    message = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

