from __future__ import unicode_literals
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field
from django import forms
from .models import Centre


# class NewCentreForm(forms.ModelForm):
#
#
#
# 	class Meta:
# 		model = Centre
# 		fields = ['name', 'description', 'location']

class NewCentreForm(forms.ModelForm):
    class Meta:
        model = Centre
        fields = [
            "name",
            # "description",
            "location",
        ]