from django.shortcuts import render

from recipebox.models import Recipe, Author
from recipebox.forms import RecipeAdd, AuthorAdd

def index(request):
    html = "index.html"
    recipe = Recipe.objects.all()
    return render(request, html, {'data':recipe})

def detail(request, id):
    html = "detail.html"
    recipes = Recipe.objects.filter(id=id)
    return render(request, html, {'recipes':recipes})

def authorview(request, id):
    html = 'authorview.html'
    author = Author.objects.filter(id=id)
    author_recipe = Recipe.objects.filter(author=id)
    return render(request, html, { 'author' : author ,  'author_recipe' : author_recipe })

def recipe_add(request):
    html = recipe_add.html
    form = RecipeAdd
    if request.method == "POST":
        pass
    else:
        form = RecipeAdd()
    return render(request, html, {"form": form})

def author_add(request): 
    html = author_add.html
    form = AuthorAdd
    if request.method =="POST":
        pass
    else:
        form = AuthorAdd()
    return render(request, html, {"form": form})