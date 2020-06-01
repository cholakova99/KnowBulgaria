from django.contrib import admin
from sightseeing.models import Location, VisitedLocation


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'photo', 'rating')


@admin.register(VisitedLocation)
class VisitedLocationAdmin(admin.ModelAdmin):
    list_display = ('user', 'visited')
