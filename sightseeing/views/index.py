from django.shortcuts import render
from sightseeing.models import Review, Location


def index(request):
    logged = request.user.is_authenticated
    locations = Location.objects.all()[:5]
    reviews = Review.objects.all()[:5]
    return render(request, 'index.html', {'locations': locations, 'reviews': reviews, 'logged': logged})
