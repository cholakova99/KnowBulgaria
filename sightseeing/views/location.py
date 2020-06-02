from django.views.generic import ListView, DetailView
from sightseeing.models import Location


class LocationListView(ListView):
    model = Location
    context_object_name = "locations"
    template_name = "locations/list.html"


class LocationDetailView(DetailView):
    model = Location
    context_object_name = "location"
    template_name = "locations/detail.html"
