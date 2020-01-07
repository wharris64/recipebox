from django.shortcuts import render, redirect, HttpResponse

from recipebox.models import Recipe, Author
from recipebox.forms import RecipeAdd, AuthorAdd, LoginUser, CreateUser
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout



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


@login_required
def recipe_add(request):
    html = "recipe_add.html"
    form = None
    if request.method == "POST":
        form = RecipeAdd(request.POST)

        if form.is_valid():
            data= form.cleaned_data
            Recipe.objects.create(
                title=data['title'],
                author=data['author'],
                description=data['description'],
                timerequired=data['timerequired'],
                instructions=data['instructions']
            )
            return redirect("/")
    else:
        form = RecipeAdd()
    return render(request, html, {"form": form})


@login_required
def author_add(request): 
    html = "author_add.html"
    form = None
    if request.user.is_staff:
        if request.method =="POST":
            
            form = AuthorAdd(request.POST)
            
            if form.is_valid():
                data = form.cleaned_data

                usermake =  User.objects.create(
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
    html = "index.html"
    return render(request, html)

def login_view(request):
    html = "user_login.html"
    form = LoginUser()
    if request.method == "POST":
        form = LoginUser(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data["username"], 
                password=data["password"]
            )
            if user:
                login(request, user)
                return redirect(request.GET.get('next', '/'))
    return render(request, html, {"form": form})

