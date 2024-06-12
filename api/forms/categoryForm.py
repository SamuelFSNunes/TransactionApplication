from django import forms

class CategoryForm(forms.Form):
    name = forms.CharField(max_length=255)
    description = forms.CharField(required=False)