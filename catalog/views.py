from django.views import generic
from .models import Item


class ItemListView(generic.ListView):
    model = Item
    template_name = 'catalog/item_list.html'