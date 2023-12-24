from django.urls import path

from .views import *

app_name = 'user_dashboard'

urlpatterns = [
    path('dashboard', user_dashboard, name = "dashboard"),
    path('delete-hotel/<slug>', delete_hote, name="delete_hotel"),
    path('edit-hotel/<slug>', edit_hotel, name="edit_hotel"),
]

