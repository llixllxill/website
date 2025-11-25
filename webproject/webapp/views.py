from django.shortcuts import render
from .models import Client, Booking, Weapon
# Create your views here.
def home(request):
    return render(request, 'home.html')

def weapons_catalog(request):
    return render(request, 'weapons_catalog.html')
