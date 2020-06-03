from django.shortcuts import render, get_object_or_404
from sightseeing.models import Review
from django import forms
from django.http import HttpResponse


def list(request):
    return render(request, 'review/list.html', {'revieww': Review.objects.all()})


def detail(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    return render(request, 'review/detail.html', {'review': review})


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('location', 'rating', 'text', 'suggest')


def add_review(request):
    if request.method == "POST":
        data = request.POST
        form = ReviewForm(data=data)
        if form.is_valid():
            new_review = form.save()
            return redirect(reverse('sightseeing:review:list'))
        else:
            return render(request, 'review/add.html', {'form':form})
    else:
        form = ReviewForm()
        return render(request, 'review/add.html', {'form':form})