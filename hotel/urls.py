from django.urls import path
from .views import *

app_name = 'hotel'

urlpatterns = [
    path("", index, name='hotel'),
    path("add-hotel", register_hotel, name='add_hotel'),
    path("hotel-detail/<slug>", hotel_detail, name='hotel_detail'),
]
