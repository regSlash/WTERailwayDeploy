from rest_framework import serializers
from .models import Meal

class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ['id', 'mealName', 'status', 'prepTime', 'yields',
                   'mealType', 'recipe', 'image', 'ingredients']