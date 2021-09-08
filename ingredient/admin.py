from django.contrib import admin
from .models import Ingredient, User_Ingredient, Recipe_Ingredient

admin.site.register(Ingredient)
admin.site.register(User_Ingredient)
admin.site.register(Recipe_Ingredient)
