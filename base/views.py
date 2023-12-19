from django.shortcuts import render, HttpResponse

from hotel.models import Hotel

# Create your views here.
def home(request):
    hotel_instance = Hotel.objects.all()
    
    context = {
        'allhotel': hotel_instance,
    }
    return render(request, 'index.html', context)

    
