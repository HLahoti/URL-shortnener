from django.forms import ModelForm
from django import forms
from .models import *

class makeShortURLForm(ModelForm):
    class Meta:
        model=lsurls
        field="__all__"
        exclude=[
            "short",
            "created",
        ]
        widgets={
            'long': forms.TextInput(
                attrs={'placeholder':'Long URL here!'}
            ),
            'nick': forms.TextInput(
                attrs={'placeholder':'Nickname your URL'}
            ),
        }
