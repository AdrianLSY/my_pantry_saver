from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
# from django.contrib.auth.models import User
from .models import UserRecipe, UserIngredient
from recipe.models import RecipeIngredient
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect


# Create your views here.


class UserLoginView(LoginView):
    template_name = 'user/login.html'
    fields = '__all__ '
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('mypantry')


class UserRegister(FormView):
    template_name = 'user/register.html'
    form_class = UserCreationForm
    # This is not working somehow
    # redirect_authenticated_user = True
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
    model = User
    template_name = 'user/mypantry.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # filtering data to get user specific data
        # context ['recipe'] =context['recipe'].filter(user=self.request.user)
        context['recipes'] = UserRecipe.objects.all().filter(user=self.request.user)
        context['ingredients'] = UserIngredient.objects.all().filter(user=self.request.user)
        # context ['ingredient'] =context['ingredient'].filter(user=self.request.user)
        return context


class UserIngredientCreate(LoginRequiredMixin, CreateView):
    model = UserIngredient
    fields = ['ingredient', 'expiry_date', 'quantity']
    template_name = 'user/user_ingredient_form.html'
    success_url = reverse_lazy('mypantry')
    context_object_name = 'ingredient_list'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.in_pantry = True
        return super(UserIngredientCreate, self).form_valid(form)


class UserIngredientUpdate(LoginRequiredMixin, UpdateView):
    model = UserIngredient
    fields = ['ingredient', 'expiry_date', 'quantity']
    template_name = 'user/user_ingredient_form.html'
    success_url = reverse_lazy('mypantry')


class UserIngredientDelete(LoginRequiredMixin, DeleteView):
    model = UserIngredient
    context_object_name = 'ingredient'
    template_name = 'user/user_ingredient_confirm_delete.html'
    success_url = reverse_lazy('mypantry')


class Pantry(LoginRequiredMixin, ListView):
    model = User
    template_name = 'user/pantry.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # filtering data to get user specific data
        # context ['recipe'] =context['recipe'].filter(user=self.request.user)
        context['recipes'] = UserRecipe.objects.all().filter(user=self.request.user)
        context['ingredients'] = UserIngredient.objects.all().filter(user=self.request.user, in_pantry=True)
        # context ['ingredient'] =context['ingredient'].filter(user=self.request.user)
        return context


class UserRecipeCreate(LoginRequiredMixin, CreateView):
    model = UserRecipe
    fields = ['recipe', 'meal']
    template_name = 'user/user_recipe_form.html'
    success_url = reverse_lazy('mypantry')
    context_object_name = 'recipe_list'

    def form_valid(self, form):
        form.instance.user = self.request.user
        user_recipe = form.save()
        print(user_recipe.recipe)
        recipe_ingredients = RecipeIngredient.objects.all().filter(recipe=user_recipe.recipe)
        for recipe_ingredient in recipe_ingredients:
            print(recipe_ingredient)
            user_ingredient = UserIngredient(
                user=self.request.user,
                user_recipe=user_recipe,
                ingredient=recipe_ingredient.ingredient,
                quantity=recipe_ingredient.quantity
            )
            user_ingredient.save()
            print(user_ingredient)

        # return reverse_lazy('mypantry')


class UserRecipeUpdate(LoginRequiredMixin, UpdateView):
    model = UserRecipe
    fields = ['recipe']
    template_name = 'user/user_recipe_form.html'
    success_url = reverse_lazy('mypantry')


class UserRecipeDelete(LoginRequiredMixin, DeleteView):
    model = UserRecipe
    context_object_name = 'recipe'
    template_name = 'user/user_recipe_confirm_delete.html'
    success_url = reverse_lazy('mypantry')


class ShoppingList(LoginRequiredMixin, ListView):
    model = UserIngredient
    template_name = 'user/shopping_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ingredients'] = UserIngredient.objects.all().filter(user=self.request.user, in_pantry=False)

        return context

def shopping_list_item_to_pantry(request, pk):
    ingredient = UserIngredient.objects.get(id=pk)
    ingredient.in_pantry = True
    ingredient.save()

    return HttpResponseRedirect(reverse_lazy('shopping-list'))
