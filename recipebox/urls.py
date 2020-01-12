from recipebox import models
from django.contrib import admin
from django.urls import path
from .views import *

admin.site.register(models.Author)
admin.site.register(models.Recipe)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('detail/<int:id>/', detail),
    path('authorview/<int:id>/', authorview),
    path('authoradd/', author_add),
    path("recipeadd/", recipe_add),
    path("login/", login_view),
    path("logout/", logout_view),
    path('editrecipe/<int:id>/', recipe_edit_view),
    path('favorite/<int:recipeId>/<int:authorId>', favorite)
]
