from django.shortcuts import render, HttpResponse, get_object_or_404
from .forms import HotelForm

from .models import Hotel

def index(request):
    return HttpResponse("hello this is hotel section")

def register_hotel(request):
    form = HotelForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            
            # Reset the form after successful submission
            form = HotelForm()

    return render(request, 'hotel/add_hotel.html', {'form': form})

def hotel_detail(request, hotel_id):
    hotel = get_object_or_404(Hotel, pk = hotel_id)

    return render(request, 'hotel/hotel_detail.html', {'hotel': hotel})