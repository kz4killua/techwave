from django import forms  # Import Django's forms module
from .models import Item  # Import the Item model

# Define a form for the Item model
class ItemForm(forms.ModelForm):
    class Meta:
        model = Item  # Associate this form with the Item model
        fields = ['name', 'stock', 'price']  # Fields to include in the form
