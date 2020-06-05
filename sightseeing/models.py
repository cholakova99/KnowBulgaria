from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


def location_directory_path(instance, filename):
    return f'location_{instance.name}/{filename}'


def profile_directory_path(instance, filename):
    return f'profile_{instance.id}/{filename}'


class Location(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    photo = models.ImageField(upload_to=location_directory_path)

    def __str__(self):
        return self.name


class PersonalLocation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, null=True, default=None)

    def __str__(self):
        return str(self.user) + ' ' + self.status + ' ' + str(self.location)


class Review(models.Model):
    rating = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)], default=0)
    text = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    suggest = models.BooleanField()


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=50, null=True, blank=True)
    photo = models.ImageField(upload_to=profile_directory_path, null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    b_day = models.DateField(blank=True, null=True)
