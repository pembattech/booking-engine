from django.db import models

# Create your models here.
class Hotel(models.Model):
    name = models.CharField(max_length = 255)
    address = models.TextField()
    description = models.TextField()
    
    def __str__(self):
        return self.name
