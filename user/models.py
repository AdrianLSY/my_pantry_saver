from django.db import models
from django import forms
from django.contrib.auth.models import User
from recipe.models import Recipe
from ingredient.models import Ingredient
# Create your models here.


#class User(models.Model):
    #user=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    #recipe = models.ManyToManyField(Recipe, through="UserRecipe")
    #ingredients = models.ForeignKey('ingredient', on_delete=models.CASCADE)
    

    #def __str__(self):
     #   return self.user

    #class Meta:
      # ordering=['id']


class UserRecipe(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete = models.CASCADE)

    class Meta:
        #constraints = [
        #    models.UniqueConstraint(fields=('recipe', 'user'), name='Recipe_per_user')
        #]
        ordering = ['recipe']
    def get(self):
        return self.recipe

class UserIngredient(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    #recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredients = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    expiry_date = models.DateField(null=True, blank=True)
    quantity = models.IntegerField(null=True)

    class Meta:
        # constraints = [
        #     models.UniqueConstraint(fields=('user_id', 'ingredients_id'), name='user_ingredients')
        # ]
        ordering = ["ingredients"]

    def get(self):
        return self.ingredients