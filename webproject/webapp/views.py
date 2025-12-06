from django.shortcuts import render, get_object_or_404
from .models import *

def index(request):
    cartridges = AmmoSales.objects.all().order_by('caliber', 'price')[:3]
    context = {'cartridges': cartridges,}
    return render(request, 'index.html', context)

def catalog(request):
    cartridges = AmmoSales.objects.all().order_by('caliber', 'price')
    
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

def ammo_detail(request, pk):
    """Детальная страница патрона через ID"""
    ammo = get_object_or_404(AmmoSales, pk=pk)
    
    similar = AmmoSales.objects.filter(caliber=ammo.caliber).exclude(pk=pk)[:4]
    
    context = {
        'ammo': ammo,
        'similar': similar,
        'price_per_round': ammo.price_per_round() if hasattr(ammo, 'price_per_round') else 0,
    }
    return render(request, 'ammo_detail.html', context)