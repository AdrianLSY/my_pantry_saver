from django.contrib import admin

# Register your models here.
from .models import UserRecipe

#admin.site.register(User)
admin.site.register(UserRecipe)