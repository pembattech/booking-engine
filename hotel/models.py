from django.db import models

from base.helper import generate_slug

# Create your models here.
class Hotel(models.Model):
    name = models.CharField(max_length = 255)
    address = models.CharField(max_length = 255)
    description = models.TextField()
    image = models.ImageField(upload_to='hotel/hotel_images/', null=True)
    price = models.IntegerField(null = True)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.name)
        super(Hotel, self).save(*args, **kwargs)
