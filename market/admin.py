from django.contrib import admin
from .models import Brand, Bike, ContactMessage, Booking

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Bike)
class BikeAdmin(admin.ModelAdmin):
    list_display = ('title','brand','model','year','price','location','is_booked')
    list_filter = ('brand','year','is_booked')
    search_fields = ('title','model','location')

admin.site.register(ContactMessage)
admin.site.register(Booking)
