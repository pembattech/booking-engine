from django.shortcuts import render, HttpResponse

from hotel.models import Hotel

# Create your views here.
def home(request):
    hotel_instance = Hotel.objects.all()
    
    context = {
        'allhotel': hotel_instance,
    }
    return render(request, 'index.html', context)

def search_hotel(request):
    location = request.GET.get('location', '')

    search_terms = location.split()
    hotel_instance = Hotel.objects.all()
    
    matching_terms = []
    for location_item in search_terms:
        for hotel in hotel_instance:
            if location_item.lower() in hotel.address.lower():
                matching_terms.append(hotel)

    return render(request, 'search_list.html', {'matching_terms': matching_terms, 'search_location': location})