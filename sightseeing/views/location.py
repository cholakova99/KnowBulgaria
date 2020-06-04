from django.views.generic import ListView
from sightseeing.models import Location, PersonalLocation, Review

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render


class LocationListView(ListView):
    model = Location
    context_object_name = "locations"
    template_name = "locations/list.html"


@login_required(login_url='sightseeing:login')
def add_to_list(request, location):
    data = request.POST
    user = request.user
    try:
        p_loc = PersonalLocation.objects.get(user=user, location=location)
        if data['status'] == 'none':
            p_loc.delete()
    except Exception:
        p_loc = PersonalLocation(user=user, location=location, status=data['status'])
    finally:
        if data['status'] != 'none':
            p_loc.save()


def detail(request, location_id):
    location = get_object_or_404(Location, id=location_id)
    reviews = Review.objects.filter(location=location)

    if request.method == "POST":
        add_to_list(request, location)
        return render(request, "locations/detail.html", {'location': location, 'reviews': reviews, 'success': True})
    else:
        return render(request, "locations/detail.html", {'location': location, 'reviews': reviews})
