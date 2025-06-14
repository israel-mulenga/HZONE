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
import messagerie.views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("", authentification.views.landing, name="landing"),
    path('admin/', admin.site.urls),
    path("connexion/", authentification.views.connexion, name="connexion"),
    path("inscription/", authentification.views.Inscription.as_view(), name="inscription"),
    path("password-forgot/", authentification.views.password_forgot, name="password-forgot"),
    path("logout/", hzone_app.views.logout_view, name="logout"),
    path("home/", hzone_app.views.home, name="home" ),
    path("favoris/", hzone_app.views.favoris, name="favoris"),
    path("listings/", hzone_app.views.listings, name="listings"),
    path("listing/<int:listing_id>/", hzone_app.views.listing_detail, name="listing_detail"),
    path("listing/update/<int:listing_id>/", hzone_app.views.listing_update, name="listing_update"),
    path("listing/delete/<int:listing_id>/", hzone_app.views.listing_delete, name="listing_delete"),
    path('messagerie/<int:listing_id>/<str:receiver_username>/', messagerie.views.chat_view, name='chat_view'),
    path('chat/messages/<int:discussion_id>/', messagerie.views.get_chat_messages, name='get_chat_messages'),  # ✅ Supprime 'receiver_username'
    path('messagerie/discussions/', messagerie.views.list_discussions, name='list_discussions'),
    
]


if settings.DEBUG :
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)