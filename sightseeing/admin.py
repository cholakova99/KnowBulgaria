from django.contrib import admin
from sightseeing.models import Location, PersonalLocation


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'photo', 'rating')


@admin.register(PersonalLocation)
class PersonalLocationAdmin(admin.ModelAdmin):
    list_display = ('user', 'visited')
