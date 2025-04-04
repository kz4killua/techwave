from django import forms
from .models import Item
from forms import CustomClearableFileInput

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'stock', 'price', 'image']
        widgets = {
            'image': CustomClearableFileInput(attrs={'class': 'custom-file-input'}),
        }
