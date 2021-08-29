from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class User(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    id= models.IntegerField(primary_key=True)
    recipe=models.ForeignKey('recipe')
    ingredient=models.ForeignKey('ingredient')


    def __str__(self):
        return self.user

    class Meta:
        ordering=['id']
        