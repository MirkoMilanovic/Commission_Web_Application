from django import forms
from .constants import COMMISSION_RATES


class RatesForm(forms.Form): 
    city = forms.ChoiceField(choices = [])

    def __init__(self, *args, **kwargs):
        super(RatesForm, self).__init__(*args, **kwargs)
        self.fields['city'].choices = [(key, key) for key in COMMISSION_RATES.keys()]