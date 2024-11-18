"""
URL configuration for puyuan project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.user, name='user'),
    path('default', views.default, name='default'),
    path('setting', views.setting, name='setting'),
    path('badge', views.badge, name='badge'),
    path('blood/pressure', views.blood_pressure, name='blood_pressure'),
    path('weight', views.weight, name='weight'),
    path('blood/sugar', views.blood_sugar, name='blood_sugar'),
    path('last-upload/', views.last_upload, name='last_upload'),
    path('diet', views.diet, name='diet'),
    path('diary/', views.diary, name='diary'),
    path('records', views.records, name='records'),
    path('a1c', views.a1c, name='a1c'),
    path('a1c/', views.a1c, name='a1c'),
    path('medical', views.medical, name='medical'),
    path('medical/', views.medical, name='medical'),
    path('drug-used', views.drug_used, name='drug_used'),
    path('care', views.care, name='care'),
    path('care/', views.care, name='care')
]
