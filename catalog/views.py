from django.views import generic
from .models import Item  # Import only the necessary models
from .filters import ItemFilter  # Import the ItemFilter
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ItemForm  # Import the correct form

class ItemListView(generic.ListView):
    model = Item
    template_name = 'catalog/item_list.html'
    context_object_name = 'item_list'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ItemFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        context['form'] = ItemForm()
        return context

    def post(self, request, *args, **kwargs):
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalog:item_list')
        return self.get(request, *args, **kwargs)

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
    return render(request, 'catalog/edit_item.html', {'form': form})

def delete_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if request.method == "POST":
        item.delete()
        return redirect('catalog:item_list')
    return render(request, 'catalog/delete_item.html', {'item': item})