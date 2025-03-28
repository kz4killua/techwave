# filepath: /c:/Users/Administrator/Documents/Ontech/Software-Design-and-Analysis/project/techwave/catalog/views.py

# Importing necessary modules and classes
from django.contrib.auth.mixins import LoginRequiredMixin  # Mixin to require user login for certain views
from django.urls import reverse  # Function to reverse resolve URLs
from django.views import generic  # Importing generic views for common patterns (e.g., ListView, CreateView)
from .models import Item  # Importing the Item model for interacting with items in the database
from .filters import ItemFilter  # Importing the filter class to apply filtering logic to the item list
from django.shortcuts import get_object_or_404, redirect  # Helper functions to get objects or redirect
from django.contrib.auth.decorators import login_required  # Decorator to enforce login
from django import forms  # Importing the forms module to handle form creation
from django.http import HttpResponseRedirect  # For handling redirects in responses
from django.urls import reverse_lazy  # For lazy URL reversing (e.g., in class-based views)
from django.shortcuts import render  # For rendering templates
from .forms import ItemForm  # Importing the form class to handle item creation and editing
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .models import Item
from django.views.generic.detail import DetailView
from .models import Item


# View for listing all items
class ItemListView(generic.ListView):
    model = Item  # The model to use for this view
    template_name = 'catalog/item_list.html'  # The template to render the item list
    context_object_name = 'item_list'  # The name to use for the list in the template

    def get_context_data(self, **kwargs):
        # Adding custom context to the view's context
        context = super().get_context_data(**kwargs)
        
        # Applying the filter to the queryset based on GET parameters
        filter = ItemFilter(self.request.GET, queryset=self.get_queryset())
        
        # Counting how many filters are applied
        filter_count = sum(any(filter.data[key]) for key in filter.data)
        
        # Adding custom context variables to be used in the template
        context['filter'] = filter
        context['filter_count'] = filter_count
        context['LoggedIn'] = True  # Indicates the user is logged in
        return context

# View for creating a new item
class ItemCreateView(LoginRequiredMixin, generic.CreateView):
    model = Item  # The model to create
    template_name = 'catalog/item_form.html'  # The template to use for item creation
    fields = ['name', 'stock', 'price', 'image']  # Include the image field

    def get_success_url(self):
        # Redirect to the item list page after a successful item creation
        return reverse('catalog:item_list')

# View for editing an existing item
@login_required
def edit_item(request, item_id):
    # Getting the item object based on its ID or returning a 404 if not found
    item = get_object_or_404(Item, pk=item_id)

    if request.method == "POST":
        # Include request.FILES to handle file uploads
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():  # If the form is valid, save the item
            form.save()
            return redirect('catalog:item_list')  # Redirect to the item list after saving
    else:
        # If not a POST request, prepopulate the form with the current item data
        form = ItemForm(instance=item)

    # Render the edit item template with the form
    return render(request, 'catalog/edit_item.html', {'form': form})


# View for deleting an existing item
@login_required  # Ensures the user must be logged in to access this view
def delete_item(request, item_id):
    # Getting the item object based on its ID or returning a 404 if not found
    item = get_object_or_404(Item, pk=item_id)

    if request.method == "POST":
        # If the form is submitted, delete the item and redirect to the item list
        item.delete()
        return redirect('catalog:item_list')

    # Render the delete confirmation template with the item to be deleted
    return render(request, 'catalog/delete_item.html', {'item': item})

class ItemDetailView(DetailView):
    model = Item
    template_name = 'catalog/item_detail.html'  # Template to render the item details
    context_object_name = 'item'  # Name of the object in the template context