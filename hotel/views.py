from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from datetime import datetime
from decimal import Decimal

from .forms import HotelForm, HotelImageFormSet, ReservationForm
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


# views.py
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from .forms import ReservationForm


@csrf_exempt  # For simplicity; consider using a proper CSRF protection method
@require_POST
def update_total_cost(request, slug):
    form = ReservationForm(request.POST)

    print(form)

    if form.is_valid():
        reservation = form.save(commit=False)
        reservation.hotel = Hotel.objects.get(slug=slug)
        tc = reservation.calculate_total_cost()
        print("pemba")
        print(reservation.calculate_total_cost())
        print(JsonResponse({"total_cost": tc}))
        print("pemba")

        return JsonResponse({"total_cost": tc})
    else:
        return JsonResponse({"error": "Invalid form data"}, status=400)


def hotel_detail(request, slug):
    hotel = get_object_or_404(Hotel, slug=slug)
    images = hotel.hotelimage_set.all()

    if request.method == "POST":
        reservation_form = ReservationForm(request.POST)
        print(reservation_form)
        if reservation_form.is_valid():
            reservation = reservation_form.save(commit=False)
            reservation.hotel = hotel
            reservation.user = request.user
            total_cost = reservation.calculate_total_cost()
            reservation.total_cost = total_cost

            reservation.save()

            return redirect("hotel:hotel")

    else:
        # Pass the hotel instance to the form
        reservation_form = ReservationForm()

    context = {"hotel": hotel, "images": images, "reservation_form": reservation_form}

    return render(request, "hotel/hotel_detail.html", context)
