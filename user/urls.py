from django.urls import path
from .views import UserLoginView, UserRegister, MyPantry, UserRecipeCreate, UserRecipeUpdate, UserRecipeDelete
from django.contrib.auth.views import LogoutView 

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='mypantry'), name='logout'),
    #path('logout/', LogoutView.as_view(next_page='login'), name='logout'), if we want to redirect to login page.
    path('register/', UserRegister.as_view(), name='register'),
    path('mypantry', MyPantry.as_view(), name= 'mypantry'),
    path('userrecipe/new', UserRecipeCreate.as_view(), name='user-add-recipe'), 
    path('user_recipe/edit/<int:pk>', UserRecipeUpdate.as_view(), name='user-edit-recipe'), 
    path('user_recipe/delete/<int:pk>', UserRecipeDelete.as_view(), name='user-delete-recipe'), 
]