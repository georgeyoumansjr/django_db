from django import forms
from .models import MockData

class MockDataForm(forms.ModelForm):
    class Meta:
        model = MockData
        fields = ['name', 'description']
