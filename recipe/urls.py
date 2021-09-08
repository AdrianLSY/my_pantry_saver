from django.urls import path
from .views import RecipeList, RecipeDetail, RecipeCreate, RecipeUpdate, RecipeDelete

urlpatterns = [
    path('recepe/', RecipeList.as_view(), name='recipelist'), 
    path('recipe/<int:pk>', RecipeDetail.as_view(), name='recipe'), 
    path('new-recipe/', RecipeCreate.as_view(), name='new-recipe'), 
    path('edit-recipe/<int:pk>', RecipeUpdate.as_view(), name='edit-recipe'), 
    path('delete-recipe/<int:pk>', RecipeDelete.as_view(), name='delete-recipe'), 
]
