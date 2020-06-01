from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

visited_choices = [("want to visit", "want to visit"), ("visited", "visited")]


class Location(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    photo = models.ImageField()


class PersonalLocation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    visited = models.CharField(max_length=50, choices=visited_choices)


class Review(models.Model):
    rating = models.FloatField([MinValueValidator(0), MaxValueValidator(5)])
    text = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    suggest = models.BooleanField()
