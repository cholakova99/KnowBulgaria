from django.shortcuts import render, get_object_or_404
from sightseeing.models import UserProfile
from django.core.exceptions import PermissionDenied
from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('address', 'photo', 'bio', 'b_day')
        widgets = {'b_day': DateInput()}


def detail(request, profile_id):
    logged = request.user.is_authenticated
    profile = get_object_or_404(UserProfile, id=profile_id)
    return render(request, 'profile/detail.html', {'logged': logged, 'profile': profile})


def update_info(request, profile_id):
    logged = request.user.is_authenticated
    profile = get_object_or_404(UserProfile, id=profile_id)
    if profile.user == request.user:
        if request.method == 'POST':
            form = ProfileForm(request.POST, request.FILES, instance=profile)
            form.save()
        else:
            form = ProfileForm(instance=profile)
        return render(request, "profile/update.html", {'form': form, 'logged': logged})
    else:
        raise PermissionDenied()
