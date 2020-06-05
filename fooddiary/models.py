from django.db import models
from django.contrib.auth.models import User
class Meal(models.Model):
    nameOfMeal = models.CharField(max_length=50)
    descriptionOfMeal = models.TextField(max_length=500, blank=True)
    date = models.DateField(auto_now_add=False ,auto_now=False, null=True, blank=True)
    favourite = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return 'Meal(date='+str(self.date)+', descriptionOfMeal='+str(self.descriptionOfMeal)
        + ', date='+str(self.date)
        + ')'


class Activity(models.Model):
    activity = models.CharField(max_length=50)
    description = models.TextField(max_length=500, blank=True)
    date = models.DateField(auto_now_add=False ,auto_now=False, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.activity