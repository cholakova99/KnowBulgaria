from django.shortcuts import render, get_object_or_404, redirect
from sightseeing.models import Review, Location
from django import forms
#from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def list(request):
    return render(request, 'review/list.html', {'review': Review.objects.all()})


def detail(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    return render(request, 'review/detail.html', {'review': review})


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('location', 'rating', 'text', 'suggest')

    # def __init__(self, user, *args, **kargs):
    #     self.user = user
    #     super().__init__(*args, **kargs)


@login_required(login_url='sightseeing:login')
def add_review(request):
    location = Location.objects.all()
    if request.method == "POST":
        data = request.POST
        form = ReviewForm(data=data)
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.user = request.user
            new_review.save()
            return redirect(reverse('sightseeing:review:list'))
        else:
            return render(request, 'review/add.html', {'form': form, 'location': location})
    else:
        form = ReviewForm()
        return render(request, 'review/add.html', {'form': form, 'location': location})
