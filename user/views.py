from django.shortcuts import render
from django.contrib.auth.views import LoginView 
from django.views.generic.edit import FormView

from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login 
from .models  import User
# Create your views here.


class UserLoginView(LoginView):
    template_name='user/login.html'
    field ='__all__ '
    redirect_authenticated_user = True
   
    


class UserRegister(FormView):
    template_name = 'user/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    
    
    
    