from ingredient.models import Ingredient
from django.shortcuts import render
from .models import Ingredient
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# A list of available ingredients, updated by Admin.
class IngredientList(LoginRequiredMixin, ListView):
    model = Ingredient
    context_object_name = 'ingredients'

# Shows the details of an ingredient.
class IngredientDetail(LoginRequiredMixin, DeleteView):
    model = Ingredient
    context_object_name = 'ingredient'
    template_name = 'ingredient/ingredient.html'

# Create an ingredient.
class IngredientCreate(LoginRequiredMixin, CreateView):
    model = Ingredient
    fields = '__all__'
    success_url = reverse_lazy('ingredients')

# Update the ingredient.
class IngredientUpdate(LoginRequiredMixin, UpdateView):
    model = Ingredient
    fields = '__all__'
    success_url = reverse_lazy('ingredients')

# Delete the ingredient.
class IngredientDelete(LoginRequiredMixin, DeleteView):
    model = Ingredient
    context_object_name = 'ingredient'
    success_url = reverse_lazy('ingredients')