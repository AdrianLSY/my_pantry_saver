from django.urls import path
from .views import RecipeList, RecipeDetail, RecipeCreate, RecipeUpdate, RecipeDelete

urlpatterns = [
    path('recipes/', RecipeList.as_view(), name='recipelist'), 
    path('recipe/<int:pk>/', RecipeDetail.as_view(), name='recipe'), 
    path('recipe/new/', RecipeCreate.as_view(), name='new-recipe'), 
    path('recipe/edit/<int:pk>/', RecipeUpdate.as_view(), name='edit-recipe'), 
    path('recipe/delete/<int:pk>/', RecipeDelete.as_view(), name='delete-recipe'), 
]
