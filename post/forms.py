from django import forms
from .models import Postmodels

class PostForm(forms.ModelForm):
    class Meta:
        model = Postmodels
        fields = ['title','media','post']

