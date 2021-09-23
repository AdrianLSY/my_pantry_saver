from django.urls import path
from .views import IngredientDetail, IngredientList, IngredientCreate, IngredientUpdate, IngredientDelete

urlpatterns = [
    path('ingredients/', IngredientList.as_view(), name='ingredients'),
    path('ingredient/<int:pk>/', IngredientDetail.as_view(), name='ingredient'),
    path('ingredient/new/', IngredientCreate.as_view(), name='new-ingredient'), 
    path('ingredient/edit/<int:pk>/', IngredientUpdate.as_view(), name='edit-ingredient'), 
    path('ingredient/delete/<int:pk>/', IngredientDelete.as_view(), name='delete-ingredient'), 
]
