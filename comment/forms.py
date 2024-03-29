from django import forms
from .models import Commentmodels

class CommentForm(forms.ModelForm):
    class Meta:
        model = Commentmodels
        fields = ('users','comment')