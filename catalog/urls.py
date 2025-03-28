# filepath: /c:/Users/Administrator/Documents/Ontech/Software-Design-and-Analysis/project/techwave/catalog/urls.py

# Importing necessary modules from Django
from django.urls import path
from . import views  # Importing the views from the current directory (catalog)

# The name of the app in the Django project, used for namespace purposes
app_name = 'catalog'

# URL patterns for the catalog app, mapping URL paths to corresponding views
urlpatterns = [
    # URL for the item list view (home page for catalog)
    path('', views.ItemListView.as_view(), name='item_list'),

    # URL for creating a new item
    path('create/', views.ItemCreateView.as_view(), name='item_create'),  # Add item URL pattern

    # URL for editing an existing item, capturing the item_id as a URL parameter
    path('edit/<int:item_id>/', views.edit_item, name='edit_item'),

    # URL for deleting an existing item, also capturing the item_id as a URL parameter
    path('delete/<int:item_id>/', views.delete_item, name='delete_item'),

    path('item/<int:pk>/', views.ItemDetailView.as_view(), name='item_detail'),  # Add this line
]
