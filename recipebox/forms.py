from django import forms
from django import ModelForm
from recipebox.models import Author
from recipebox.models import Recipe 
# model form need below
class RecipeAdd(ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'author', 'description', 'timerequired', 'instructions']
    
    

class AuthorAdd(forms.Form):
    name = forms.CharField(max_length = 50)
    biosection = forms.TextField()
