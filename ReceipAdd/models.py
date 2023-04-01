from django.db import models
from django import forms
from django.forms import FileInput
from django.contrib.postgres.fields import ArrayField

class Meal(models.Model):
    STATUS_CHOICES = (
        ('t', 'Tried and true'),
        ('w', 'Wishlist'),
    )

    MEAL_TYPE = (
        ('b', 'Breakfast'),
        ('e', 'Elevenses'),
        ('l', 'Lunch'),
        ('s', 'Supper'),
        ('d', 'Dinner'),

    )

    mealName = models.CharField(max_length=255)
    status = models.CharField(max_length=255, choices= STATUS_CHOICES)
    prepTime = models.IntegerField()
    yields = models.IntegerField()
    mealType = models.CharField(max_length=255, choices=MEAL_TYPE)
    recipe = models.CharField(max_length=255)
    image = models.ImageField()
    ingredients = ArrayField(models.CharField(max_length=50), blank=False, null=False)

class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ['mealName','status','prepTime','yields',
                  'mealType','recipe','image']
        widgets = {
            'image':FileInput(),
        }