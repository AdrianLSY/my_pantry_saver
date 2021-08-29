from ingredient.models import Ingredient
from django.shortcuts import render
from .models import Ingredient
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class IngredientList(ListView):
    model = Ingredient

class IngredientDetail(DeleteView):
    model = Ingredient  
    