from django.shortcuts import render, redirect, get_object_or_404
from .forms import HotelForm

from .models import Hotel, HotelImage

def index(request):
    hotel_instance = Hotel.objects.all()
    
    context = {
        'allhotel': hotel_instance,
    }
    return render(request, 'index.html', context)

def register_hotel(request):
    if request.method == 'POST':
        form = HotelForm(request.POST, request.FILES)
        if form.is_valid():
            hotel_instance = form.save(commit=False)
            hotel_instance.save()

            for uploaded_file in request.FILES.getlist('images'):
                hotelimage_instance = HotelImage.objects.create(image=uploaded_file)
                hotel_instance.images.add(hotelimage_instance)
            
            hotel_instance.save()
            
            return redirect('hotel:hotel_detail', slug=hotel_instance.slug)
        else:
            # Handle the case where no files were submitted
            return render(request, 'add_hotel.html', {'form': form, 'error': 'Please select images to upload'})
    else:
        form = HotelForm()

    return render(request, 'hotel/add_hotel.html', {'form': form})

def hotel_detail(request, slug):
    hotel = get_object_or_404(Hotel, slug=slug)
    images = hotel.images.all()

    return render(request, 'hotel/hotel_detail.html', {'hotel': hotel, 'images': images})
