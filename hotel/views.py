from django.shortcuts import render, HttpResponse, get_object_or_404
from .forms import HotelForm

from .models import Hotel

def index(request):
    hotel_instance = Hotel.objects.all()
    
    for i in hotel_instance:
        print(i.image)
    
    context = {
        'allhotel': hotel_instance,
    }
    return render(request, 'index.html', context)

def register_hotel(request):
    form = HotelForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            
            # Reset the form after successful submission
            form = HotelForm()

    return render(request, 'hotel/add_hotel.html', {'form': form})

def hotel_detail(request, slug):
    hotel = get_object_or_404(Hotel, slug = slug)
    
    print(hotel.image)

    return render(request, 'hotel/hotel_detail.html', {'hotel': hotel})