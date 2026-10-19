from django.contrib import admin
from .models import Application, Company
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
 list_display=("name","owner","location","created_at")
 search_fields=("name","owner__username")
@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
 list_display=("role","company","owner","status","applied_on")
 list_filter=("status",)
 search_fields=("role","company__name","owner__username")
