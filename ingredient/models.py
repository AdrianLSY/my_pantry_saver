from django.db import models
from recipe.models import Recipe
from user.models import User

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    type = models.IntegerField(blank=False)
    datetime = models.DateField(blank=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name'] # Also can be sorted by primary_id

class User_Ingredient(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    ingredient= models.ForeignKey(Ingredient, on_delete = models.SET_NULL)

    def __str__(self):
        return self.name

class Recipe_Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete = models.CASCADE)
    ingredient= models.ForeignKey(Ingredient, on_delete = models.SET_NULL)

    def __str__(self):
        return self.name