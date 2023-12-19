from django.shortcuts import render, HttpResponse
from .forms import HotelForm

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
