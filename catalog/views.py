from django.views import generic
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Item
from .filters import ItemFilter
from .forms import ItemForm


class ItemListView(generic.ListView):
    model = Item
    template_name = 'catalog/item_list.html'
    context_object_name = 'item_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Add filter data to context
        filter = ItemFilter(self.request.GET, queryset=self.get_queryset())
        filter_count = sum(any(filter.data[key]) for key in filter.data)
        context['filter'] = filter
        context['filter_count'] = filter_count
        context['LoggedIn'] = True  # Call to the isLoggedIn method with False as an argument
        return context
    

class ItemCreateView(generic.CreateView):
    model = Item
    template_name = 'catalog/item_form.html'
    fields = ['name', 'stock', 'price']

    def get_success_url(self):
        return reverse('catalog:item_list')


def edit_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('catalog:item_list')
    else:
        form = ItemForm(instance=item)
    return render(request, 'catalog/edit_item.html', {'form': form, "variable": ItemListView.isLoggedIn(False)})


def delete_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if request.method == "POST":
        item.delete()
        return redirect('catalog:item_list')
    return render(request, 'catalog/delete_item.html', {'item': item})