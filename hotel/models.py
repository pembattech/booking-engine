from django.db import models
from django.contrib.auth.models import User

from base.helper import generate_slug  # Import the generate_slug function

# Create your models here.


class Hotel(models.Model):
    hotelier = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    slug = models.SlugField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = generate_slug(self.name)
        super(Hotel, self).save(*args, **kwargs)


class HotelImage(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    hotel_images = models.ImageField(upload_to="hotel/hotel_images/")

    def __str__(self):
        return f"Images for {self.hotel.name}"
