from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView 

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='mypantry'), name='logout'),
    #path('logout/', LogoutView.as_view(next_page='login'), name='logout'), if we want to redirect to login page.
    path('register/', UserRegister.as_view(), name='register'),
    
    path('mypantry/', MyPantry.as_view(), name= 'mypantry'),
    path('mypantry/recipe/new/', UserRecipeCreate.as_view(), name='user-add-recipe'), 
    path('mypantry/recipe/edit/<int:pk>/', UserRecipeUpdate.as_view(), name='user-edit-recipe'), 
    path('mypantry/recipe/delete/<int:pk>/', UserRecipeDelete.as_view(), name='user-delete-recipe'),
    path('mypantry/ingredient/new/', UserIngredientCreate.as_view(), name='user-add-ingredient'), 
    path('mypantry/ingredient/edit/<int:pk>/', UserIngredientUpdate.as_view(), name='user-edit-ingredient'), 
    path('mypantry/ingredient/delete/<int:pk>/', UserIngredientDelete.as_view(), name='user-delete-ingredient'), 
]