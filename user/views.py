from django.shortcuts import render
from django.contrib.auth.views import LoginView 
from django.views.generic import FormView


from django.contrib.auth.views import LoginView 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login 
from .models  import User
# Create your views here.


class UserLoginView(LoginView):
    template_name='base/login.html'
    field ='__all__ '
    redirect_authenticated_user = True
    sucess_url =
    


class UserRegister(FormView):
    template_name = 'base/register'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    sucess_url =
    