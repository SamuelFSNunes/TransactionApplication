from django import forms
from api.models import User

class UserForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    password = forms.CharField(min_length=6)