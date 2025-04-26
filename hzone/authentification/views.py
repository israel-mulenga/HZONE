from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.views.generic import View 
from django.contrib import messages

class Inscription(View):
    User = get_user_model()
    home_page = 'hzone_app/home.html'
    inscription_page = 'authentification/inscription.html'

    def get(self, request):
        return render(request, self.inscription_page)

    def post(self, request):
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        username = request.POST.get("username")
        password = request.POST.get("password")
        repeatpassword = request.POST.get("repeatpassword")
        phonenumber = request.POST.get("phone_number")
        profilephoto = request.FILES.get("profile_photo")

        if password != repeatpassword:
            messages.error(request, "Les mots de passe ne correspondent pas.")
            return self.get(request)
        elif self.User.objects.filter(username=username).exists():
            messages.error(request, "Ce nom d'utilisateur est déjà utilisé.")
            return self.get(request)
        else:
            user = self.User.objects.create_user(
                username=username, 
                first_name=firstname, 
                last_name=lastname,
                password=password,
                phone_number=phonenumber,
                profile_photo=profilephoto
            )
            login(request, user)
            return redirect('home')

def landing(request):
    return render(request, 'authentification/index.html')



def connexion(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect")
    return render(request, 'authentification/connexion.html')



def password_forgot(request):
    return render(request, "authentification/password_forgot.html")

