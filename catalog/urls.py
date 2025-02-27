from django.urls import path

from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.ItemListView.as_view(), name='item_list'),
    path('create/', views.ItemCreateView.as_view(), name='item_create'),
    path('edit/<int:item_id>/', views.edit_item, name='edit_item'),
]