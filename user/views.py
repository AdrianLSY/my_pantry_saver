from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls.base import is_valid_path, reverse
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from ingredient.models import Ingredient
# from django.contrib.auth.models import User
from .models import UserRecipe, UserIngredient
from recipe.models import RecipeIngredient, Recipe
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, request




li = []

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
        context['days'] = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
        context['meals'] = ["BREAKFAST", "LUNCH", "DINNER"]
        # context ['ingredient'] =context['ingredient'].filter(user=self.request.user)
        return context


class UserIngredientCreate(LoginRequiredMixin, CreateView):
    model = UserIngredient
    fields = ['ingredient', 'expiry_date', 'quantity', 'unit']
    template_name = 'user/user_ingredient_form.html'
    success_url = reverse_lazy('pantry')
    context_object_name = 'ingredient_list'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.in_pantry = True
        return super(UserIngredientCreate, self).form_valid(form)


class UserIngredientUpdate(LoginRequiredMixin, UpdateView):
    model = UserIngredient
    fields = ['ingredient', 'expiry_date', 'quantity']
    template_name = 'user/user_ingredient_form.html'
    success_url = reverse_lazy('pantry')


class UserIngredientDelete(LoginRequiredMixin, DeleteView):
    model = UserIngredient
    context_object_name = 'ingredient'
    template_name = 'user/user_ingredient_confirm_delete.html'
    success_url = reverse_lazy('pantry')


class Pantry(LoginRequiredMixin, ListView):
    model = UserIngredient
    template_name = 'user/pantry.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # filtering data to get user specific data
        # context ['recipe'] =context['recipe'].filter(user=self.request.user)
        context['recipes'] = UserRecipe.objects.all().filter(user=self.request.user)
        context['ingredients'] = UserIngredient.objects.all().filter(user=self.request.user, in_pantry=True)
        context['fridge'] = UserIngredient.objects.all().filter(user=self.request.user, ingredient__place_in='FRIDGE', in_pantry=True)
        context['pantry'] = UserIngredient.objects.all().filter(user=self.request.user, ingredient__place_in='PANTRY', in_pantry=True)
        context['freezer'] = UserIngredient.objects.all().filter(user=self.request.user, ingredient__place_in='FREEZER', in_pantry=True)
        # context ['ingredient'] =context['ingredient'].filter(user=self.request.user)
        return context


class UserRecipeCreate(LoginRequiredMixin, CreateView):
    model = UserRecipe
    fields = ['recipe', 'meal', 'day']
    template_name = 'user/user_recipe_form.html'
    success_url = reverse_lazy('mypantry')
    context_object_name = 'recipe_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        a = set(Recipe.objects.all())
        context['meals'] = ["BREAKFAST", "LUNCH", "DINNER"]
        context['recipes'] = a
        context['recipe_ingredients'] = RecipeIngredient.objects.all().filter()
        return context
        
    def form_valid(self, form):
        form.instance.user = self.request.user
        user_recipe = form.save()
        print(user_recipe.recipe)
        recipe_ingredients = RecipeIngredient.objects.all().filter(recipe=user_recipe.recipe)
        for recipe_ingredient in recipe_ingredients:
            user_ingredient = UserIngredient(
                user=self.request.user,
                user_recipe=user_recipe,
                ingredient=recipe_ingredient.ingredient,
                quantity=recipe_ingredient.quantity,
                unit=recipe_ingredient.unit
            )
            user_ingredient.save()
            print(user_ingredient)

        # return reverse_lazy('mypantry')
        return super(UserRecipeCreate, self).form_valid(form)

class UserRecipeDetail(LoginRequiredMixin, DetailView):
    model = UserRecipe
    context_object_name = 'recipe'
    template_name = 'user/user_recipe_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipe_ingredients'] = RecipeIngredient.objects.all().filter()
        return context

class UserRecipeUpdate(LoginRequiredMixin, UpdateView):
    model = UserRecipe
    fields = ['meal', 'day']
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
        global li
        context = super().get_context_data(**kwargs)
        
        i = UserIngredient.objects.all().filter(user=self.request.user)
        
        recipes = UserRecipe.objects.all().filter(user=self.request.user)
        ingredients = []
        for r in recipes.iterator():
            recipe_ingredient = RecipeIngredient.objects.all().filter(recipe_id=r.recipe.id)
            for all in recipe_ingredient.iterator():
                for aa in i.iterator():
                    if r.id == aa.user_recipe.id and all.ingredient.id == aa.ingredient.id and all.quantity == aa.quantity and all.unit == aa.unit: 
                        recipe_ingredient = RecipeIngredient.objects.all().filter(recipe_id=r.recipe.id).exclude(ingredient_id=all.ingredient.id)
                    
            ingredients.append(recipe_ingredient)
       
        context['recipe_ingredients'] = ingredients
        return context


def shopping_list_item_to_pantry(request, pk):
    ingredient = UserIngredient.objects.get(id=pk)
    ingredient.in_pantry = True
    ingredient.save()

    return HttpResponseRedirect(reverse_lazy('shopping-list'))


class UserIngredientShoppingCreate(LoginRequiredMixin, CreateView):
    model = UserIngredient
    fields = ['user_recipe', 'ingredient', 'expiry_date', 'quantity', 'unit']
    template_name = 'user/test_form.html'
    success_url = reverse_lazy('shopping-list')
    context_object_name = 'ingredient_list'
    a = []

    def get_context_data(self, **kwargs):
        global li
        
        context = super().get_context_data(**kwargs)
        
        context['ingredient'] = RecipeIngredient.objects.all().filter(ingredient_id=self.kwargs['ingredientName'])[0].ingredient
        
        context['quantity'] = self.kwargs['quantity']
        context['unit'] = self.kwargs['unit']
        context['recipe'] = self.kwargs['recipeName']
        context['test'] = str(self.kwargs['recipeName']) + '-' + str(self.kwargs['ingredientName'])
        self.a.append(RecipeIngredient.objects.all().filter(ingredient_id=self.kwargs['ingredientName'])[0])
        self.a.append(self.kwargs['quantity'])
        self.a.append(self.kwargs['unit'])
        self.a.append(self.kwargs['recipeName'])
        return context

    def form_valid(self, form):
        global li
        recipeId = w = self.request.POST.get('recipe')
        recipe = UserRecipe.objects.all().filter(recipe_id=recipeId, user=self.request.user)[0]
        y = self.request.POST.get('expiry_date')
        x = self.request.POST.get('quantity')
        z = self.request.POST.get('unit')
        w = self.request.POST.get('ingredient')
        u = RecipeIngredient.objects.all().filter(ingredient_id=w)[0].ingredient
        
        li.append(w)
        
        form.instance.user = self.request.user
        form.instance.user_recipe = recipe
        form.instance.ingredient = u
        form.instance.quantity = x
        form.instance.unit = z
        form.instance.expiry_date = y
        form.instance.in_pantry = True
        
      
       
        return super(UserIngredientShoppingCreate, self).form_valid(form)


    

    #def form_invalid(self, form):
        # This method is called when invalid form data has been POSTed.
        y = self.request.POST.get('expiry_date')
        x = self.request.POST.get('quantity')
        z = self.request.POST.get('unit')
        w = self.request.POST.get('ingredient')
        u = RecipeIngredient.objects.all().filter(ingredient_id=w)[0].ingredient
        t = UserIngredient(user=self.request.user, ingredient=u, expiry_date=y, quantity=x, unit=z, in_pantry=True)
        t.save()
        return render('user/test_form.html', {'test': str(self.a[3]) + "-"+ str(self.a[0].ingredient.id)})
        return HttpResponseRedirect('shopping-list')