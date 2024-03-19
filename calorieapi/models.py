# calorieapi/models.py

from django.db import models

class FoodItem(models.Model):
    name = models.CharField(max_length=100, unique=True)
    calories = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'calorieapi'


# Create your models here.
