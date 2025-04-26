from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Listing, ListingImage
from django.contrib.auth import logout

@login_required(login_url="connexion")
def home(request):
    listings = Listing.objects.all()
    return render(request, 'hzone_app/home.html', context={'listings' : listings})

@login_required
def favoris(request):
    return render(request, 'hzone_app/favoris.html')

@login_required
def listings(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        description = request.POST.get("description")
        transaction_type = request.POST.get("transactionType")
        surface = request.POST.get("surface")
        number_of_pieces = request.POST.get("number_of_pieces")
        property_type = request.POST.get("propertyType")
        outdoor_space = request.POST.get("outdoorSpace")
        city = request.POST.get("city")
        district = request.POST.get("district")
        street = request.POST.get("street")
        street_number = request.POST.get("streetNumber")

        price = request.POST.get("price")
        

        listing = Listing.objects.create(
            owner=request.user,
            title=title,
            description=description,
            transaction_type=transaction_type,
            surface=surface,
            number_of_piece=number_of_pieces,
            outdoor_space=outdoor_space,
            city=city,
            district=district,
            street=street,
            street_number=street_number,
            price=price,
            property_type=property_type
        )
        
        images = request.FILES.getlist('images')
        for image in images:
           listing_image = ListingImage.objects.create(listing=listing, image=image)
           listing_image.save()
        listing.save()

    

    listings = Listing.objects.filter(owner=request.user).order_by('-create_at')
    context = {
        'listings': listings
    }
    return render(request, 'hzone_app/listings.html', context)     




@login_required(login_url="connexion")
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('connexion')
    

