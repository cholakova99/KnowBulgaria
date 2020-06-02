from django.contrib import admin
from sightseeing.models import Location, PersonalLocation, Review


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'photo')


@admin.register(PersonalLocation)
class PersonalLocationAdmin(admin.ModelAdmin):
    list_display = ('user', 'location', 'visited')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('location', 'text', 'rating', 'suggest', 'user')
