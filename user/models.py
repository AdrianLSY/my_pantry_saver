from django.db import models
from django import forms
from django.contrib.auth.models import User
# Create your models here.


class User(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    


    def __str__(self):
        return self.user

    class Meta:
        ordering=['id']
        