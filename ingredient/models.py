from django.db import models

LOCATION = (
    ('PANTRY', 'pantry'),
    ('FRIDGE', 'fridge'),
    ('FREEZER', 'freezer')
)

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    place_in = models.CharField(max_length = 255, choices = LOCATION, default = 'PANTRY')
    expirey_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name'] # Also can be sorted by primary_id