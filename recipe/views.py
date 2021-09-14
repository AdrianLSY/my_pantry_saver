from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from ingredient.models import Ingredient
from .models import Recipe, RecipeIngredient, User, UserRecipe

class RecipeList(ListView):
    model = Recipe
    context_object_name = 'recipes'

class UserList(ListView):
    model = User
    context_object_name = 'users'

class UserDetail(DetailView):
    model = User
    context_object_name = 'user'
    template_name = 'recipe/user.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ingredients'] = []
        context['set_recipe'] = UserRecipe.objects.values_list(user=context['user'])
        for i in context['set_recipe']:
            print(i)
            context['ingredients'].append(RecipeIngredient.objects.all().filter(recipe=i))
        return context

class RecipeDetail(DetailView):
    model = Recipe
    context_object_name = 'recipe'
    template_name = 'recipe/recipe.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['set_recipe'] = RecipeIngredient.objects.all().filter(recipe=context['recipe'])
        return context

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
