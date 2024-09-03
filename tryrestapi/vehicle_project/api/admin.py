from django.contrib import admin
from .models import Vehicle

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('rnr', 'kurzname', 'info', 'lagerort', 'hu') 
    search_fields = ('kurzname', 'info') 
