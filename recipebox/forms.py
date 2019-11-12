from django import forms
from django.forms import ModelForm
from recipebox.models import Author
from recipebox.models import Recipe 
# model form need below
class RecipeAdd(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'author', 'description', 'timerequired', 'instructions']
    
    
# found code for biosection at https://stackoverflow.com/a/7302919

class AuthorAdd(forms.Form):
    name = forms.CharField(max_length = 50)
    biosection = forms.Textarea()
