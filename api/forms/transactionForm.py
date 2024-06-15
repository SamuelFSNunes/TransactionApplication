from django import forms
from api.models.modelCategory import Category
from api.repository.repository import Repository

class TransactionForm(forms.Form):
    category = forms.ChoiceField(choices=[])
    amount = forms.FloatField()
    date = forms.DateTimeField(widget=forms.DateInput(attrs={'type': 'date'}))
    description = forms.CharField(max_length=255, required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        repository = Repository(Category, 'categories')
        categories = repository.get_all()
        self.fields['category'].choices = [(category.id, category.name) for category in categories]
