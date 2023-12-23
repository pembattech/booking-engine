from django.urls import path
from .views import home, search_hotel, login_user, register_user, logout_user

urlpatterns = [
    path("", home, name="home"),
    path("login", login_user, name="login"),
    path("register", register_user, name="register"),
    path("logout", logout_user, name="logout"),
    path("search/", search_hotel, name="search"),
    
]
