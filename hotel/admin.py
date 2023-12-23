from django.contrib import admin

from .models import *


class HotelAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name", )}
# Register your models here.
admin.site.register(Hotel, HotelAdmin)
admin.site.register(HotelImage)
