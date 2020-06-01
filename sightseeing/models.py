from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Location(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    photo = models.ImageField()
    rating = models.FloatField([MinValueValidator(0), MaxValueValidator(5)])


class VisitedLocation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    visited = models.ForeignKey(Location, on_delete=models.CASCADE)
