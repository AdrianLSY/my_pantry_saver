from django.db import models

# Create your models here.
class Ingredient(models.Model):
    primary = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100) 
    type = models.IntegerField(blank=False)

    def __str__(self):
        return self.name

    class Meta:
        order = ['primary'] # Also can be sorted by name