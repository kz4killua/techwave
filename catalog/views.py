from django.views import generic
from .models import Item
from django.urls import reverse


class ItemListView(generic.ListView):
    model = Item
    template_name = 'catalog/item_list.html'


class ItemCreateView(generic.CreateView):
    model = Item
    template_name = 'catalog/item_form.html'
    fields = ['name', 'stock', 'price']

    def get_success_url(self):
        return reverse('item_list')