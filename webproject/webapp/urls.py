from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('catalog', views.catalog, name='catalog'),
    path('backet', views.backet, name='backet'),
    path('ammo/<int:pk>/', views.ammo_detail, name='ammo_detail'),
]