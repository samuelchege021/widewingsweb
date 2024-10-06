from django.contrib import admin
from .models import Plumbing, Biodigester, WaterTreatment, SolarInstallation, ContactMessage

@admin.register(Plumbing)
class PlumbingAdmin(admin.ModelAdmin):
    list_display = ('name', 'pub_date')
    search_fields = ('name', 'description')
    list_filter = ('pub_date',)

@admin.register(Biodigester)
class BiodigesterAdmin(admin.ModelAdmin):
    list_display = ('name', 'pub_date')
    search_fields = ('name', 'description')
    list_filter = ('pub_date',)

@admin.register(WaterTreatment)
class WaterTreatmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'pub_date')
    search_fields = ('name', 'description')
    list_filter = ('pub_date',)

@admin.register(SolarInstallation)
class SolarInstallationAdmin(admin.ModelAdmin):
    list_display = ('name', 'pub_date')
    search_fields = ('name', 'description')
    list_filter = ('pub_date',)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date_sent')
    search_fields = ('name', 'email', 'message')
    list_filter = ('date_sent',)
