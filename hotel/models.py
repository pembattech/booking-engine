from django.db import models

from base.helper import generate_slug

# Create your models here.

class HotelImage(models.Model):
    image = models.FileField(upload_to='hotel/hotel_images/')

    
class Hotel(models.Model):
    name = models.CharField(max_length = 255)
    address = models.CharField(max_length = 255)
    description = models.TextField()
    images = models.ManyToManyField(HotelImage, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.name)
        super(Hotel, self).save(*args, **kwargs)