from django.db import models
from django.db.models.deletion import DO_NOTHING
from ingredient.models import Ingredient

MEAL = (
    ('BREAKFAST', 'breakfast'),
    ('LUNCH', 'lunch'),
    ('DINNER', 'dinner')
)

# Recipe model.
class Recipe(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.ManyToManyField(Ingredient, through="RecipeIngredient")
    instructions = models.TextField(null=True, blank=True)
    meal = models.CharField(max_length=255, choices=MEAL, default='BREAKFAST')
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=5)
    time = models.IntegerField(default=10)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

# Model of recipe with ingredients.
class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    unit = models.CharField(max_length=255, null=True, blank=True)

    def get(self):
        return self.recipe
