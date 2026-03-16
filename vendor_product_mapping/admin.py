from django.contrib import admin # type: ignore
from .models import VendorProductMapping

@admin.register(VendorProductMapping)
class VendorProductMappingAdmin(admin.ModelAdmin):
    list_display = ('vendor','product','primary_mapping','is_active','created_at','updated_at')
    list_filter = ('primary_mapping','is_active')
    search_fields = ('vendor__name','product__name')
    
