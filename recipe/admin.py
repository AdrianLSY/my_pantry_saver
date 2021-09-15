from django.contrib import admin
from .models import Recipe, RecipeIngredient, User, UserRecipe

admin.site.register(User)
admin.site.register(Recipe)
admin.site.register(RecipeIngredient)
admin.site.register(UserRecipe)