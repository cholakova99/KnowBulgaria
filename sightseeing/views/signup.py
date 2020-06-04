from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from sightseeing.models import UserProfile


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            profile = UserProfile(user=user)
            profile.save()
            login(request, user)
            return redirect('sightseeing:index')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
