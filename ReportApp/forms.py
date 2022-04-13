from django import forms
from django.core import validators
from . import views


class RatesForm(forms.Form): 
    rates = forms.ChoiceField(choices = [])

    def __init__(self, *args, **kwargs):
        super(RatesForm, self).__init__(*args, **kwargs)
        self.fields['rates'].choices = [(key, key) for key, value in views.commission_rates.items()]