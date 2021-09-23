
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
#from django.contrib.auth.models import User
from .models import UserRecipe, UserIngredient
from django.views.generic.list import ListView 
from django.contrib.auth.models import User

# Create your views here.


class UserLoginView(LoginView):
    template_name='user/login.html'
    fields ='__all__ '
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('mypantry')
    
    

class UserRegister(FormView):
    template_name = 'user/register.html'
    form_class = UserCreationForm
    #This is not working somehow
    #redirect_authenticated_user = True 
    success_url = reverse_lazy('mypantry')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(UserRegister, self).form_valid(form)

    def get(self, *args, **kwargs):
         if self.request.user.is_authenticated:
             return redirect('mypantry')
         return super(UserRegister, self).get(*args, **kwargs)
    


class MyPantry(LoginRequiredMixin, ListView):
#class MyPantry(LoginRequiredMixin, ListView): if we want login required for the main page.
    model = User
    template_name = 'user/mypantry.html'
    context_object_name = 'user'
    

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        #filtering data to get user specific data
        #context ['recipe'] =context['recipe'].filter(user=self.request.user)
        context['recipes'] = UserRecipe.objects.all().filter(user=self.request.user)
        context['ingredients'] = UserIngredient.objects.all().filter(user=self.request.user)
        #context ['ingredient'] =context['ingredient'].filter(user=self.request.user)
        return context 
    
class UserRecipeCreate(CreateView):
    model = UserRecipe
    fields = ['recipe']
    template_name = 'user/user_recipe_form.html'
    success_url = reverse_lazy('mypantry')
    context_object_name = 'recipe_list'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(UserRecipeCreate, self).form_valid(form)

class UserRecipeUpdate(UpdateView):
    model = UserRecipe
    fields = ['recipe']
    template_name = 'user/user_recipe_form.html'
    success_url = reverse_lazy('mypantry')

class UserRecipeDelete(DeleteView):
    model = UserRecipe
    context_object_name = 'recipe'
    template_name = 'user/user_recipe_confirm_delete.html'
    success_url = reverse_lazy('mypantry')  

class UserIngredientCreate(CreateView):
    model = UserIngredient
    fields = ['ingredients', 'expiry_date', 'quantity']
    template_name = 'user/user_ingredient_form.html'
    success_url = reverse_lazy('mypantry')
    context_object_name = 'ingredient_list'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(UserIngredientCreate, self).form_valid(form)

class UserIngredientUpdate(UpdateView):
    model = UserIngredient
    fields = ['ingredients', 'expiry_date', 'quantity']
    template_name = 'user/user_ingredient_form.html'
    success_url = reverse_lazy('mypantry')

class UserIngredientDelete(DeleteView):
    model = UserIngredient
    context_object_name = 'ingredient'
    template_name = 'user/user_ingredient_confirm_delete.html'
    success_url = reverse_lazy('mypantry')