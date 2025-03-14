# filepath: /c:/Users/Administrator/Documents/Ontech/Software-Design-and-Analysis/project/techwave/catalog/views.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views import generic
from .models import Item
from .filters import ItemFilter
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import render
from .forms import ItemForm


class ItemListView(generic.ListView):
    model = Item
    template_name = 'catalog/item_list.html'
    context_object_name = 'item_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        filter = ItemFilter(self.request.GET, queryset=self.get_queryset())
        filter_count = sum(any(filter.data[key]) for key in filter.data)
        context['filter'] = filter
        context['filter_count'] = filter_count
        context['LoggedIn'] = True
        return context

class ItemCreateView(LoginRequiredMixin, generic.CreateView):
    model = Item
    template_name = 'catalog/item_form.html'
    fields = ['name', 'stock', 'price']

    def get_success_url(self):
        return reverse('catalog:item_list')

@login_required
def edit_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    # Your edit item logic here
    item = get_object_or_404(Item, pk=item_id)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('catalog:item_list')
    else:
        form = ItemForm(instance=item)
    return render(request, 'catalog/edit_item.html', {'form': form})

@login_required
def delete_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if request.method == "POST":
        item.delete()
        return redirect('catalog:item_list')
    return render(request, 'catalog/delete_item.html', {'item': item})