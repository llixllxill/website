from django.contrib import admin

from .models import Client, Target, Service, Weapon, Staff, Booking, AmmoSales

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'email')
    search_fields = ('first_name', 'last_name', 'email')

@admin.register(Target)
class TargetAdmin(admin.ModelAdmin):
    list_display = ('name', 'target_type', 'difficulty_level')
    list_filter = ('target_type', 'difficulty_level')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_name', 'price', 'duration_minute')
    list_filter = ('price',)

@admin.register(Weapon)
class WeaponAdmin(admin.ModelAdmin):
    list_display = ('weapon_name', 'weapon_type', 'caliber', 'status')
    list_filter = ('weapon_type', 'status')

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'hire_date')
    search_fields = ('first_name', 'last_name')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('client', 'staff', 'booking_date', 'start_time', 'total_price')
    list_filter = ('booking_date', 'service')
    date_hierarchy = 'booking_date'

@admin.register(AmmoSales)
class AmmoSalesAdmin(admin.ModelAdmin):
    list_display = ('booking', 'caliber', 'quantity', 'total_amount', 'sale_date')
    list_filter = ('sale_date', 'caliber')