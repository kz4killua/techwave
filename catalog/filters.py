import django_filters

from .models import Item

class ItemFilter(django_filters.FilterSet):

    # Filtering by values
    name_icontains = django_filters.CharFilter(field_name='name', lookup_expr='icontains', label='Name contains')
    stock_lt = django_filters.NumberFilter(field_name='stock', lookup_expr='lt', label='Stock is less than')
    stock_gt = django_filters.NumberFilter(field_name='stock', lookup_expr='gt', label='Stock is greater than')
    price_lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt', label='Price is less than')
    price_gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt', label='Price is greater than')

    # Sorting by values
    ordering = django_filters.OrderingFilter(
        fields=(
            ('name', 'name'),
            ('stock', 'stock'),
            ('price', 'price'),
        ),
        field_labels={
            'name': 'Name',
            'stock': 'Stock',
            'price': 'Price',
        },
        label='Sort by',
    )

    class Meta:
        model = Item
        fields = ['ordering', 'name_icontains', 'stock_lt', 'stock_gt', 'price_lt', 'price_gt']