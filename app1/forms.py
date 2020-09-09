from django import forms
from .models import Pricing_table


class PricingForm(forms.ModelForm):
    Created_Date = forms.DateField(required=False)
    Updated_Date = forms.DateField(required=False)

    class Meta:
        model=Pricing_table
        fields="__all__"
