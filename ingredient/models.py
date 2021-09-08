from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    # recipe = models.ForeignKey('recipe')
    type = models.IntegerField(blank=False)
    datetime = models.DateField(blank=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name'] # Also can be sorted by primary_id