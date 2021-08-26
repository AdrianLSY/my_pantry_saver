from django.urls import path
from .views import RecipeList

urlpatterns = [
    path('', RecipeList.as_view(), name='recipe'), 
]
