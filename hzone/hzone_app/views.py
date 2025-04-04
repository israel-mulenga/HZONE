from django.shortcuts import render

def landing(request):
    return render(request, 'hzone_app/index.html')
