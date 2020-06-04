from django.db.models import Avg, Count, Q
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render

from sightseeing.models import Location, PersonalLocation, Review


def sort_locations(by, user):
    if by == 'name':
        return Location.objects.all().order_by('name')
    elif by == 'rating':
        return Location.objects.all().\
            annotate(avg_rating=Avg('review__rating')).\
            order_by('-avg_rating')
    elif by == 'reviews':
        return Location.objects.all().\
            annotate(rev_count=Count('review')).\
            order_by('-rev_count')
    elif by == 'visited':
        return Location.objects.all().\
            annotate(times_visited=Count('personallocation', filter=Q(personallocation__status__exact='visited'))).\
            order_by('-times_visited')
    elif by == 'wanted':
        return Location.objects.all().\
            annotate(wanted=Count('personallocation', filter=Q(personallocation__status__exact='want'))).\
            order_by('-wanted')
    elif by == 'my_visited':
        return Location.objects.\
            filter(personallocation__user=user, personallocation__status__exact='visited')
    elif by == 'want':
        return Location.objects.\
            filter(personallocation__user=user, personallocation__status__exact='want')


def list(request):
    logged = request.user.is_authenticated
    if request.method == "POST":
        locations = sort_locations(request.POST['sort'], request.user)
    else:
        locations = Location.objects.all()
    return render(request, "locations/list.html", {'locations': locations, 'logged': logged})


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
    logged = request.user.is_authenticated
    location = get_object_or_404(Location, id=location_id)
    reviews = Review.objects.filter(location=location)

    if request.method == "POST":
        add_to_list(request, location)
        return render(request, "locations/detail.html", {'location': location, 'reviews': reviews, 'success': True, 'logged': logged})
    else:
        return render(request, "locations/detail.html", {'location': location, 'reviews': reviews, 'logged': logged})
