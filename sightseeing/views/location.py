from django.views.generic import ListView
from sightseeing.models import Location


class LocationListView(ListView):
    model = Location
    context_object_name = "locations"
    template_name = "locations.html"
