from django.db import models
from ingredient.models import Ingredient

# Create your models here.

class Recipe(models.Model):
    #id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    ingredients = models.TextField(null=True, blank=True)
    #ingredients = models.ForeignKey('ingredient', on_delete=models.CASCADE)
    instructions = models.TextField(null=True, blank=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1) # rating 1.0 - 5.0

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name'] # May be order by rating


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete = models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete = models.DO_NOTHING)
    quantity = models.IntegerField(default=1)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=('recipe', 'ingredient'), name='Recipe_per_ingredien')
        ]

    def get(self):
        return self.recipe