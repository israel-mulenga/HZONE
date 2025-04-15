from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url="connexion")
def home(request):
    return render(request, 'hzone_app/home.html')


