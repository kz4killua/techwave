# catalog/filters.py
import django_filters
from .models import Item

class ItemFilter(django_filters.FilterSet):
    stock_lt = django_filters.NumberFilter(field_name='stock', lookup_expr='lt', label='Stock less than')
    stock_gt = django_filters.NumberFilter(field_name='stock', lookup_expr='gt', label='Stock greater than')
    price_lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt', label='Price less than')
    price_gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt', label='Price greater than')
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains', label='Name contains')

    class Meta:
        model = Item
        fields = {
            'name': ['icontains'],
            'price': [],
            'stock': [],
        }