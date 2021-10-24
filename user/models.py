from django.db import models
from django import forms
from django.contrib.auth.models import User
from recipe.models import Recipe
from ingredient.models import Ingredient

# Meal of the day.
MEAL = (
    ('BREAKFAST', 'breakfast'),
    ('LUNCH', 'lunch'),
    ('DINNER', 'dinner')
)

# Days of the week.
DAY = (
    ('MONDAY', 'monday'),
    ('TUESDAY', 'tuesday'),
    ('WEDNESDAY', 'wednesday'),
    ('THURSDAY', 'thursday'),
    ('FRIDAY', 'friday'),
    ('SATURDAY', 'saturday'),
    ('SUNDAY', 'sunday')
)

# This model is user's meal plan.
class UserRecipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    meal = models.CharField(max_length=255, choices=MEAL, default='BREAKFAST')
    day = models.CharField(max_length=255, choices=DAY, default='MONDAY')

    class Meta:
        ordering = ['recipe']

    def get(self):
        return self.recipe

# This model is the user's pantry.
class UserIngredient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_recipe = models.ForeignKey(UserRecipe, on_delete=models.CASCADE, blank=True, null=True)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    expiry_date = models.DateField(null=True, blank=True)
    quantity = models.IntegerField(null=True)
    unit = models.CharField(max_length=255, blank=True, null=True)
    in_pantry = models.BooleanField(default=False)

    class Meta:
        ordering = ["ingredient"]

    def get(self):
        return self.ingredient
