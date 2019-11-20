from django import forms
from django.forms import ModelForm
from recipebox.models import Author
from recipebox.models import Recipe 
from django.contrib.auth.models import User
# model form need below
class RecipeAdd(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'author', 'description', 'timerequired', 'instructions']
    
    
# found code for biosection at https://stackoverflow.com/a/7302919

class AuthorAdd(forms.Form):
    username = forms.CharField(min_length = 5, max_length = 22)
    password = forms.CharField(min_length =  4)
    name = forms.CharField(max_length = 50)
    biosection = forms.Textarea()

class CreateUser(forms.Form):
    user = forms.CharField(min_length = 5, max_length = 22)
    password = forms.CharField(min_length =  4)

class LoginUser(forms.Form):
    username = forms.CharField(min_length = 5, max_length = 22)
    password = forms.CharField(min_length =  4)
