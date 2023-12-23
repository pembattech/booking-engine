from django.shortcuts import render, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required

from hotel.models import Hotel

# Create your views here.
@login_required(login_url='login')
def user_dashboard(request):
    hotels = Hotel.objects.filter(hotelier=request.user)

    context = {
        'hotels': hotels
    }
    
    return render(request, 'user_dashboard/user_dashboard.html', context)

@login_required(login_url='login')
def delete_hote(request, slug):
    hotel = Hotel.objects.get(slug = slug)
    hotel.delete()

    hotels = Hotel.objects.filter(hotelier=request.user)

    context = {
        'hotels': hotels
    }
    
    return render(request, 'user_dashboard/user_dashboard.html', context)
    