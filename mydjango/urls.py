"""mydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from controller1 import PageController as pc
from controller1 import testcontroller  as tc
from controller1 import UserController as uc
urlpatterns = [
    path('admin/', admin.site.urls),
    path("goA/",pc.go_a),
    path("",pc.go_login),
    path("reJson/",tc.re_json),
    path("login/",uc.login)

]
