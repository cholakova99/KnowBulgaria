from django.shortcuts import render
from sightseeing.models import Review, Location


def index(request):
    locations = Location.objects.all()[:5]
    reviews = Review.objects.all()[:5]
    return render(request, 'index.html', {'locations': locations, 'reviews': reviews})
