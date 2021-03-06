from django.contrib import admin
from sightseeing.models import Location, PersonalLocation, Review, UserProfile
from django.contrib.auth.models import User


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'photo')


@admin.register(PersonalLocation)
class PersonalLocationAdmin(admin.ModelAdmin):
    list_display = ('user', 'location', 'status')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('location', 'text', 'rating', 'suggest', 'user')


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'photo', 'bio', 'b_day')

