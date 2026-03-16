from django.contrib import admin # type: ignore
from .models import CourseCertificationMapping

@admin.register(CourseCertificationMapping)
class CourseCertificationMappingAdmin(admin.ModelAdmin):
    list_display = ('course','certification','primary_mapping','is_active','created_at','updated_at')
    list_filter = ('primary_mapping','is_active')
    search_fields = ('course__name','certification__name')
