import django_filters  # Import Django Filters package for filtering querysets
from .models import Item  # Import the Item model to apply filtering on it

# Define a filter set for the Item model
class ItemFilter(django_filters.FilterSet):

    # Filtering by values (case-insensitive name search, stock, and price ranges)
    name_icontains = django_filters.CharFilter(
        field_name='name', 
        lookup_expr='icontains',  # Case-insensitive substring match
        label='Name contains'
    )
    stock_lt = django_filters.NumberFilter(
        field_name='stock', 
        lookup_expr='lt',  # Stock is less than the given value
        label='Stock is less than'
    )
    stock_gt = django_filters.NumberFilter(
        field_name='stock', 
        lookup_expr='gt',  # Stock is greater than the given value
        label='Stock is greater than'
    )
    price_lt = django_filters.NumberFilter(
        field_name='price', 
        lookup_expr='lt',  # Price is less than the given value
        label='Price is less than'
    )
    price_gt = django_filters.NumberFilter(
        field_name='price', 
        lookup_expr='gt',  # Price is greater than the given value
        label='Price is greater than'
    )

    # Sorting options
    ordering = django_filters.OrderingFilter(
        fields=(
            ('name', 'name'),  # Sort by name
            ('stock', 'stock'),  # Sort by stock
            ('price', 'price'),  # Sort by price
        ),
        field_labels={  # Custom labels for sorting dropdown
            'name': 'Name',
            'stock': 'Stock',
            'price': 'Price',
        },
        label='Sort by',  # Label for the sorting option
    )

    class Meta:
        model = Item  # Specify the model on which filters apply
        fields = ['ordering', 'name_icontains', 'stock_lt', 'stock_gt', 'price_lt', 'price_gt']
        # Defines the fields that users can filter and sort by
