from django.shortcuts import render
from django.contrib.auth.views import LoginView 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView

from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login 
from .models  import User
from django.views.generic.list import ListView 
from django.urls import reverse_lazy

# Create your views here.


class UserLoginView(LoginView):
    template_name='user/login.html'
    fields ='__all__ '
    redirect_authenticated_user = True
    success_url = reverse_lazy('user/mypantry.html')
    

class UserRegister(FormView):
    template_name = 'user/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True


class MyPantry(LoginRequiredMixin, ListView):
    model = User 
    template_name = 'mypantry '

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context ['recipe'] =context['recipe'].filter(user=self.request.user)
        context ['ingredient'] =context['ingredient'].filter(user=self.request.user)
        return context 
    
    