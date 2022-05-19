from .models import Journal
from django import forms
class JournalForm(forms.ModelForm):
    class Meta:
        model=Journal
        fields = fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'date_created': forms.HiddenInput(),
        }
