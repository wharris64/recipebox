from django.shortcuts import render, redirect, HttpResponse

from recipebox.models import Recipe, Author
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


def index(request):
    html = "index.html"
    recipe = Recipe.objects.all()
    return render(request, html, {'data': recipe, 'user': request.user})


def detail(request, id):
    html = "detail.html"
    recipes = Recipe.objects.filter(id=id)
    print(request.user.is_authenticated)
    print(request.user)

    return render(request, html, {'recipes': recipes, 'user': request.user})


def authorview(request, id):
    html = 'authorview.html'
    author = Author.objects.get(id=id)
    author_recipe = Recipe.objects.filter(author=id)
    favorites = author.favorites.all()
    return render(request, html, {'author': author,  'author_recipe': author_recipe, 'user': request.user, 'favorites':favorites})


@login_required
def recipe_add(request):
    html = "recipe_add.html"
    form = None
    if request.method == "POST":
        form = RecipeAdd(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            Recipe.objects.create(
                title=data['title'],
                author=data['author'],
                description=data['description'],
                timerequired=data['timerequired'],
                instructions=data['instructions']
            )
            return render(request, "thanks.html")
    else:
        form = RecipeAdd()
    return render(request, html, {"form": form})


def author_add(request):
    html = "author_add.html"
    form = None
    if request.user.is_staff:
        if request.method == "POST":

            form = AuthorAdd(request.POST)

            if form.is_valid():
                data = form.cleaned_data

                usermake = User.objects.create(
                    username=data['username'],
                    password=data['password']
                )
                Author.objects.create(
                    name=data['name'],
                    user=usermake
                )

            return render(request, "thanks.html")
        else:
            form = AuthorAdd()
    else:
        return HttpResponse("Sorry bud, can't even do it!")
    return render(request, html, {"form": form})


def logout_view(request):
    logout(request)
    return redirect('/')


def login_view(request):
    html = "user_login.html"
    form = LoginUser()
    if request.method == "POST":
        form = LoginUser(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data["username"], password=data["password"])
            if user:
                login(request, user)
            return redirect(request.GET.get("next", '/'))
    return render(request, html, {"form": form})


@login_required
def recipe_edit_view(request, id):
    html = "edit_form.html"
    recipe = Recipe.objects.get(pk=id)
    if not request.user.is_staff:
        if not request.user == recipe.author:
            return redirect(request.GET.get('next', '/'))

    form = RecipeEdit(initial={
    'title': recipe.title, 
    'author': recipe.author,
    'description': recipe.description,
    'timerequired': recipe.timerequired,
    'instructions': recipe.instructions
    })
    if request.method == "POST":
        form = RecipeEdit(request.POST)
        if form.is_valid():
            form = RecipeEdit(request.POST, instance=recipe)
            form.save()
        return redirect(request.GET.get('next', '/'))

    return render(request, html, {'form':form})

def favorite(request, recipeId, authorId):
    r = Recipe.objects.get(pk=recipeId)
    author = Author.objects.get(pk=authorId)
    author.favorites.add(r)
    return redirect(request.GET.get("next", '/'))