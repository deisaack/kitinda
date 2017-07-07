from django import forms
from kitinda.productions.models import Supply

class SupplyForm(forms.ModelForm):
    class Meta:
        model = Supply
        fields = ['received_by', 'quantity']
