from django.urls import path
from .views import index, register_hotel

urlpatterns = [
    path("", index, name='hotel'),
    path("add-hotel", register_hotel, name='add_hotel'),
]
