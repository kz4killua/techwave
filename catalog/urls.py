# filepath: /c:/Users/Administrator/Documents/Ontech/Software-Design-and-Analysis/project/techwave/catalog/urls.py
from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.ItemListView.as_view(), name='item_list'),
    path('create/', views.ItemCreateView.as_view(), name='item_create'),  # Add item URL pattern
    path('edit/<int:item_id>/', views.edit_item, name='edit_item'),
    path('delete/<int:item_id>/', views.delete_item, name='delete_item'),
]