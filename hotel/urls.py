from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name='hotel'),
    path("add-hotel", register_hotel, name='add_hotel'),
    path("hotel-detail/<hotel_id>", hotel_detail, name='hotel_detail'),
]
