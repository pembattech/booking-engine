from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from hotel.models import Hotel
from hotel.forms import HotelForm, HotelImageFormSet


# Create your views here.
@login_required(login_url="login")
def user_dashboard(request):
    hotels = Hotel.objects.filter(hotelier=request.user)

    context = {"hotels": hotels}

    return render(request, "user_dashboard/user_dashboard.html", context)


@login_required(login_url="login")
def delete_hote(request, slug):
    hotel = Hotel.objects.get(slug=slug)
    hotel.delete()

    hotels = Hotel.objects.filter(hotelier=request.user)

    context = {"hotels": hotels}

    return render(request, "user_dashboard/user_dashboard.html", context)


@login_required(login_url="login")
def edit_hotel(request, slug):
    hotel_instance = get_object_or_404(Hotel, slug=slug)

    if request.method == "POST":
        hotel_form = HotelForm(request.POST, instance=hotel_instance)
        hotelimg_formset = HotelImageFormSet(
            request.POST, request.FILES, instance=hotel_instance
        )

        if hotel_form.is_valid() and hotelimg_formset.is_valid():
            hotel = hotel_form.save()

            hotelimg_formset.instance = hotel
            hotelimg_formset.save()

            return redirect("hotel:hotel_detail", slug=slug)
    else:
        hotel_form = HotelForm(instance=hotel_instance)
        hotelimg_formset = HotelImageFormSet(instance=hotel_instance)

    context = {
        "hotel_form": hotel_form,
        "hotelimg_formset": hotelimg_formset,
    }
    return render(request, "user_dashboard/edit_hotel.html", context)
