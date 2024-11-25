from django import forms
from .models import GuestBook

class GuestBookForm(forms.ModelForm):
    class Meta:
        model = GuestBook
        fields = ['name', 'address', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Address', 'rows': 3}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Message', 'rows': 5}),
        }
