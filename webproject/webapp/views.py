from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    cartridges = AmmoSales.objects.all().order_by('caliber', 'price')[:3]
    context = {'cartridges': cartridges,}
    return render(request, 'index.html', context)

def catalog(request):
    cartridges = AmmoSales.objects.all().order_by('caliber', 'price')
    
    # Добавляем методы для отображения
    for cartridge in cartridges:
        cartridge.get_name_display_name = cartridge.get_name_display_name
        cartridge.get_caliber_display_name = cartridge.get_caliber_display_name
        cartridge.price_per_round = cartridge.price_per_round
    
    context = {
        'cartridges': cartridges,
    }
    return render(request, 'catalog.html', context)

def backet(request):
    return render(request, 'backet.html')
