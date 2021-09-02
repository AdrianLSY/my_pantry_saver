from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Recipe

class RecipeList(ListView):
    model = Recipe
    context_object_name = 'recipes'

class RecipeDetail(DetailView):
    model = Recipe
    context_object_name = 'recipe'
    template_name = 'recipe/recipe.html'

class RecipeCreate(CreateView):
    model = Recipe
    fields = '__all__'
    success_url = reverse_lazy('recipelist')

class RecipeUpdate(UpdateView):
    model = Recipe
    fields = '__all__'
    success_url = reverse_lazy('recipelist')

class RecipeDelete(DeleteView):
    model = Recipe
    context_object_name = 'recipe'
    success_url = reverse_lazy('recipelist')
