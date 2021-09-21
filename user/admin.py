from django.contrib import admin

# Register your models here.
from .models import UserRecipe, UserIngredient

#admin.site.register(User)
admin.site.register(UserRecipe)
admin.site.register(UserIngredient)
