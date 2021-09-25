from django.urls import path
from .views import RecipeList, RecipeDetail, RecipeCreate, RecipeUpdate, RecipeDelete,\
    RecipeIngredientCreate, RecipeIngredientUpdate, RecipeIngredientDelete

urlpatterns = [
    path('recipes/', RecipeList.as_view(), name='recipelist'), 
    path('recipe/<int:pk>/', RecipeDetail.as_view(), name='recipe'),
    path('recipe/new/', RecipeCreate.as_view(), name='new-recipe'), 
    path('recipe/edit/<int:pk>/', RecipeUpdate.as_view(), name='edit-recipe'),
    path('recipe/delete/<int:pk>/', RecipeDelete.as_view(), name='delete-recipe'),

    path('recipe/<int:pk>/ingredient/new/', RecipeIngredientCreate.as_view(), name='new-recipe-ingredient'),
    path('recipe/<int:pk>/ingredient/<int:RecipeIngredient_pk>/edit/', RecipeIngredientUpdate.as_view(),
         name='edit-recipe-ingredient'),
    path('recipe/<int:pk>/ingredient/<int:RecipeIngredient_pk>/delete/', RecipeIngredientDelete.as_view(),
         name='delete-recipe-ingredient')
]
