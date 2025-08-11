import django_filters
from .models import Product


class PF(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr="icontains", label="название")
    price_gte = django_filters.NumberFilter(field_name="price", lookup_expr='gte', label='цена от')
    price_lte = django_filters.NumberFilter(field_name="price", lookup_expr='lte', label='цена до')
    
    class Meta:
        model = Product
        fields =['title', 'price_gte', 'price_lte']