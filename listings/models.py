# listings/models.py

from django.db import models
from django.conf import settings


class Listing(models.Model):
    BLOCK_CHOICES = [
        ('A', 'Block A'),
        ('B', 'Block B'),
        ('C', 'Block C'),
        ('D', 'Block D'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='listings')  # <-- Added this
     
    rent = models.DecimalField(max_digits=10, decimal_places=2)
    number_of_rooms = models.PositiveIntegerField()
    location = models.CharField(max_length=100, default='Bashundhara')
    block = models.CharField(max_length=1, choices=BLOCK_CHOICES)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class ListingImage(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='listings/images/')

