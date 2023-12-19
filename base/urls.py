from django.urls import path
from .views import home, search_hotel

urlpatterns = [
    path("", home, name="home"),
    path("search/", search_hotel, name="search"),
]
