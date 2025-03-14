import django_filters

from .models import Item

class ItemFilter(django_filters.FilterSet):
    name_icontains = django_filters.CharFilter(field_name='name', lookup_expr='icontains', label='Name contains')
    stock_lt = django_filters.NumberFilter(field_name='stock', lookup_expr='lt', label='Stock is less than')
    stock_gt = django_filters.NumberFilter(field_name='stock', lookup_expr='gt', label='Stock is greater than')
    price_lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt', label='Price is less than')
    price_gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt', label='Price is greater than')

    class Meta:
        model = Item
        fields = ['name_icontains', 'stock_lt', 'stock_gt', 'price_lt', 'price_gt']