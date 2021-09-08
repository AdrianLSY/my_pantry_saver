from django.urls import path
from .views import IngredientDetail, IngredientList, IngredientCreate, IngredientUpdate, IngredientDelete

urlpatterns = [
    path('ingredients/', IngredientList.as_view(), name='ingredients'),
    path('ingredient/<int:pk>/', IngredientDetail.as_view(), name='ingredient'),
    path('new-ingredient/', IngredientCreate.as_view(), name='new-ingredient'), 
    path('edit-ingredient/<int:pk>', IngredientUpdate.as_view(), name='edit-ingredient'), 
    path('delete-ingredient/<int:pk>', IngredientDelete.as_view(), name='delete-ingredient'), 
]
