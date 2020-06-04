from django.shortcuts import render, get_object_or_404, redirect
from sightseeing.models import Review, Location
from django import forms
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def list(request):
    logged = request.user.is_authenticated
    return render(request, 'review/list.html', {'review': Review.objects.all(), 'logged': logged})


def detail(request, review_id):
    logged = request.user.is_authenticated
    review = get_object_or_404(Review, id=review_id)
    all_reviews = Review.objects.filter(location=review.location).exclude(id=review.id)
    return render(request, 'review/detail.html', {'review': review, 'all_reviews': all_reviews, 'logged': logged})


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('location', 'rating', 'text', 'suggest')


@login_required(login_url='sightseeing:login')
def add_review(request):
    logged = request.user.is_authenticated
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
            return render(request, 'review/add.html', {'form': form, 'location': location, 'logged': logged})
    else:
        form = ReviewForm()
        return render(request, 'review/add.html', {'form': form, 'location': location, 'logged': logged})
