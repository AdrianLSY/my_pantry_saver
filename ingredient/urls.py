from django.urls import path
from .views import IngredientDetail, IngredientList

urlpatterns = [
    path('', IngredientList.as_view(), name='ingredients'),
    path('ingredient/<int:pk>/', IngredientDetail.as_view(), name='ingredient')
]
