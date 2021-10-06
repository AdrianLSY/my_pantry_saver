from django.db import models
from django import forms
from django.contrib.auth.models import User
from recipe.models import Recipe
from ingredient.models import Ingredient

# Create your models here.


# class User(models.Model):
# user=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
# recipe = models.ManyToManyField(Recipe, through="UserRecipe")
# ingredients = models.ForeignKey('ingredient', on_delete=models.CASCADE)


# def __str__(self):
#   return self.user

# class Meta:
# ordering=['id']


MEAL = (
    ('BREAKFAST', 'breakfast'),
    ('LUNCH', 'lunch'),
    ('DINNER', 'dinner')
)

DAY = (
    ('MONDAY', 'monday'),
    ('TUESDAY', 'tuesday'),
    ('WEDNESDAY', 'wednesday'),
    ('THURSDAY', 'thursday'),
    ('FRIDAY', 'friday'),
    ('SATURDAY', 'saturday'),
    ('SUNDAY', 'sunday')
)


class UserRecipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    meal = models.CharField(max_length=255, choices=MEAL, default='BREAKFAST')
    day = models.CharField(max_length=255, choices=DAY, default='MONDAY')

    class Meta:
        # constraints = [
        #    models.UniqueConstraint(fields=('recipe', 'user'), name='Recipe_per_user')
        # ]
        ordering = ['recipe']

    def get(self):
        return self.recipe


class UserIngredient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_recipe = models.ForeignKey(UserRecipe, on_delete=models.CASCADE, blank=True, null=True)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    expiry_date = models.DateField(null=True, blank=True)
    quantity = models.IntegerField(null=True)
    in_pantry = models.BooleanField(default=False)

    class Meta:
        # constraints = [
        #     models.UniqueConstraint(fields=('user_id', 'ingredients_id'), name='user_ingredients')
        # ]
        ordering = ["ingredient"]

    def get(self):
        return self.ingredient
