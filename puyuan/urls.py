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
from django.contrib import admin
from django.urls import path, include
from accounts.views import register, auth, send, forgot, reset, verification_check, register_check
from other.views import news, share
from user.views import user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register', register, name='register'),
    path('api/register/check/', register_check, name='register_check'),
    path('api/auth', auth, name='auth'),
    path('api/verification/send', send, name='send'),
    path('api/verification/check', verification_check, name='verification_check'),
    path('api/password/forgot', forgot, name='forgot'),
    path('api/password/reset', reset, name='reset'),
    path('api/user', user, name='user'),
    path('api/user/', include('user.urls')),
    path('api/friend/', include('friend.urls')),
    path('api/news', news, name='news'),
    path('api/share', share, name='share'),
    path('api/share/<int:data_type>', share, name='share')
]