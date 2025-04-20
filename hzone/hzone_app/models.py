from django.db import models
from authentification.models import User

class Listing(models.Model):
    TRANSACTION_CHOICES = [
        ('vente', 'Vente'),
        ('location', 'Location'),
    ]

    PROPERTY_TYPE_CHOICES = [
        ('maison', 'Maison'),
        ('appartement', 'Appartement'),
        ('terrain', 'Terrain')
    ]
    OUTDOOR_CHOICES = [
        ('oui', 'Oui'),
        ('non', 'Non'),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_CHOICES)
    property_type = models.CharField(max_length=50, choices=PROPERTY_TYPE_CHOICES)
    title = models.fields.CharField(max_length=100)
    surface = models.DecimalField(max_digits=10, decimal_places=2)
    number_of_piece = models.IntegerField()
    outdoor_space = models.CharField(max_length=3, choices=OUTDOOR_CHOICES)
    city = models.CharField()
    district = models.CharField()
    street = models.CharField(blank=True, null=True)
    street_number = models.CharField()
    description = models.TextField()
    price = models.BigIntegerField()
    create_at = models.DateTimeField(auto_now_add=True)


class ListingImage(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='listing_images/')
    uplaoaded_at = models.DateTimeField(auto_now_add=True)
