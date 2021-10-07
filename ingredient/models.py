from django.db import models

LOCATION = (
    ('PANTRY', 'pantry'),
    ('FRIDGE', 'fridge'),
    ('FREEZER', 'freezer')
)

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    # recipe = models.ForeignKey('recipe')
    place_in = models.CharField(max_length = 255, choices = LOCATION, default = 'PANTRY')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name'] # Also can be sorted by primary_id