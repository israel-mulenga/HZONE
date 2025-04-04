from django.shortcuts import render

def landing(request):
    return render(request, 'hzone_app/index.html')

def connexion(request):
    return render(request, 'hzone_app/connexion.html')

def inscription(request):
    return render(request, 'hzone_app/inscription.html')

def password_forgot(request):
    return render(request, "hzone_app/password_forgot.html")