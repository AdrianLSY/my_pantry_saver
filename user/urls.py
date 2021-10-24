from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView 

# urls related to the user.
urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='mypantry'), name='logout'),
    path('register/', UserRegister.as_view(), name='register'),
    path('mypantry/', MyPantry.as_view(), name='mypantry'),
    path('mypantry/pantry/', Pantry.as_view(), name='pantry'),
    path('mypantry/shopping-list/', ShoppingList.as_view(), name='shopping-list'),
    path('mypantry/recipe/new/', UserRecipeCreate.as_view(), name='user-add-recipe'), 
    path('mypantry/recipe/<int:pk>/view/', UserRecipeDetail.as_view(), name='user-view-recipe'),
    path('mypantry/recipe/<int:pk>/edit/', UserRecipeUpdate.as_view(), name='user-edit-recipe'),
    path('mypantry/recipe/<int:pk>/delete/', UserRecipeDelete.as_view(), name='user-delete-recipe'),
    path('mypantry/recipe/<int:pk>/complete/', user_complete_recipe, name='user-complete-recipe'),
    path('mypantry/ingredient/new/', UserIngredientCreate.as_view(), name='user-add-ingredient'), 
    path('mypantry/ingredient/<int:pk>/edit/', UserIngredientUpdate.as_view(), name='user-edit-ingredient'),
    path('mypantry/ingredient/<int:pk>/delete/', UserIngredientDelete.as_view(), name='user-delete-ingredient'),
    path('mypantry/ingredient/<int:ingredientName>/<int:quantity>/<str:unit>/pantry/', UserIngredientShoppingCreate.as_view(), name='user-pantry-shopping-ingredient')
]