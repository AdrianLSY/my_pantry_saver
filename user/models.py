from django.db import models
from django import forms
from django.contrib.auth.models import User
from recipe.models import Recipe
# Create your models here.


class User(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    #recipe = models.ForeignKey('recipe', on_delete=models.CASCADE)
    #ingredients = models.ForeignKey('ingredient', on_delete=models.CASCADE)
    

    def __str__(self):
        return self.user

    #class Meta:
    #    ordering=['id']


class UserRecipe(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.DO_NOTHING)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=('recipe', 'user'), name='Recipe_per_user')
        ]

    def get(self):
        return self.recipe

