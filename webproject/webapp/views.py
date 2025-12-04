from django.shortcuts import render
from .models import Client, Booking, Weapon, AmmoSales
# Create your views here.
def index(request):
    cartridges = AmmoSales.objects.all().order_by('caliber', 'price')[:6]
    context = {'cartridges': cartridges,}
    return render(request, 'index.html', context)

def catalog(request):
    return render(request, 'catalog.html')

def backet(request):
    return render(request, 'backet.html')
