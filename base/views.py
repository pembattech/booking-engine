from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

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

def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def logout_user(request):
    if request.user.is_authenticated:
        username = request.user.username
        logout(request)
        return redirect("home")
    else:
        return render(request, '404.html')

def login_user(request):
    if request.method == "POST":
        try:
            fetch_username = request.POST["username"]
            fetch_password = request.POST["password"]
            user = authenticate(
                request, username=fetch_username, password=fetch_password
            )
            if user is not None:
                login(request, user)

                return redirect("home")
            else:
                return HttpResponse("Invalid credentials.")
        except Exception as e:
            return HttpResponse("Error occur in login.")
    else:
        return render(request, "login.html")
