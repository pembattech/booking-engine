from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import HotelForm, HotelImageFormSet

from .models import Hotel, HotelImage


def index(request):
    hotel_instance = Hotel.objects.all()

    context = {
        "allhotel": hotel_instance,
    }
    return render(request, "index.html", context)


@login_required(login_url="login")
def register_hotel(request):
    if request.method == "POST":
        hotel_form = HotelForm(request.POST)
        hotelimg_formset = HotelImageFormSet(request.POST, request.FILES)

        if hotel_form.is_valid() and hotelimg_formset.is_valid():
            hotel = hotel_form.save(commit=False)
            hotel.hotelier = request.user
            hotel.save()
            
            hotelimg_formset.instance = hotel
            hotelimg_formset.save()

            return redirect("hotel:hotel_detail", slug=hotel.slug)

    else:
        hotel_form = HotelForm()
        hotelimg_formset = HotelImageFormSet(instance=None)

    context = {
        "hotel_form": hotel_form,
        "hotelimg_formset": hotelimg_formset,
    }

    return render(request, "hotel/add_hotel.html", context)


def hotel_detail(request, slug):
    hotel = get_object_or_404(Hotel, slug=slug)
    images = hotel.hotelimage_set.all()

    return render(
        request, "hotel/hotel_detail.html", {"hotel": hotel, "images": images}
    )
