"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path

#importตามชื่อที่เราตั้ง
from myapp.views import RegisterUserView
from myapp.views import LoginView
from myapp.views import LogoutView
urlpatterns = [
    path('admin/', admin.site.urls),
    #ตั้งชื่อpathแล้วแต่ชอบ  ตามด้วยชื่อ viewที่สร้างสร้างใน views.py
    path('registeration/', RegisterUserView, name='register_user'),
    path('login/', LoginView, name='login'),
    path('logout/', LogoutView, name='logout'),
]
