from django.shortcuts import render

from recipebox.models import Recipe, Author


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
