from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

def landing(request):
    return render(request, 'authentification/index.html')

def connexion(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Bienvenue {user.username}")
            return redirect('home')
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect")
    return render(request, 'authentification/connexion.html')

def inscription(request):
    return render(request, 'authentification/inscription.html')

def password_forgot(request):
    return render(request, "authentification/password_forgot.html")
