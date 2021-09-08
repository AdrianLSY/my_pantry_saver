from ingredient.models import Ingredient
from django.shortcuts import render
from .models import Ingredient
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class IngredientList(ListView):
    model = Ingredient
    context_object_name = 'ingredients'

class IngredientDetail(DeleteView):
    model = Ingredient
    context_object_name = 'ingredient'
    template_name = 'ingredient/ingredient.html'

class IngredientCreate(CreateView):
    model = Ingredient
    fields = '__all__'
    success_url = reverse_lazy('ingredients')

class IngredientUpdate(UpdateView):
    model = Ingredient
    fields = '__all__'
    success_url = reverse_lazy('ingredients')

class IngredientDelete(DeleteView):
    model = Ingredient
    context_object_name = 'ingredient'
    success_url = reverse_lazy('ingredients')