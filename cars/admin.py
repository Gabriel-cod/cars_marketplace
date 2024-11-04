from django.contrib import admin
from .models import *

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'plate', 'value')
    search_fields = ('model', 'brand', 'plate')

class CarInventoryAdmin(admin.ModelAdmin):
    list_display = ('cars_count', 'cars_value', 'created_at')
    search_fields = ('created_at',)

admin.site.register(Brand, BrandAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(CarInventory, CarInventoryAdmin)
