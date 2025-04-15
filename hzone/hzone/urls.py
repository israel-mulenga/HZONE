"""
URL configuration for hzone project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
import hzone_app.views
import authentification.views

urlpatterns = [
    path("", authentification.views.landing, name="landing"),
    path('admin/', admin.site.urls),
    path("connexion/", authentification.views.connexion, name="connexion"),
    path("inscription/", authentification.views.Inscription.as_view(), name="inscription"),
    path("password-forgot/", authentification.views.password_forgot, name="password-forgot"),
    path("logout/", authentification.views.logout_user, name="logout"),
    path("home/", hzone_app.views.home, name="home" )
]
