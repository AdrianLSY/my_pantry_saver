from django.db import models

# Ingredient category
LOCATION = (
    ('PANTRY', 'pantry'),
    ('FRIDGE', 'fridge'),
    ('FREEZER', 'freezer')
)

# Ingredient model
class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    place_in = models.CharField(max_length = 255, choices = LOCATION, default = 'PANTRY')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name'] # Also can be sorted by primary_id