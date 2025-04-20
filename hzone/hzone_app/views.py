from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Listing

@login_required(login_url="connexion")
def home(request):
    listings = Listing.objects.all()
    return render(request, 'hzone_app/home.html', context={'listings' : listings})

@login_required
def favoris(request):
    return render(request, 'hzone_app/favoris.html')

@login_required
def listings(request):
    return render(request, 'hzone_app/listings.html')