from django_filters import rest_framework as filters
from ..models import Product, ProductReview, Order, ProductsForOrder, ProductsCollection


class ProductFilter(filters.FilterSet):
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')
    description = filters.CharFilter(field_name='description', lookup_expr='icontains')

    class Meta:
        model = Product
        fields = {'price': ['lte', 'gte'], }


class ProductReviewFilter(filters.FilterSet):
    created_at_after = filters.DateFilter(field_name="created_at", lookup_expr='gte')
    created_at_before = filters.DateFilter(field_name="created_at", lookup_expr='lte')

    class Meta:
        model = ProductReview
        fields = ('customer', 'created_at', 'product', )


class OrderFilter(filters.FilterSet):
    created_at_after = filters.DateFilter(field_name="created_at", lookup_expr='gte')
    created_at_before = filters.DateFilter(field_name="created_at", lookup_expr='lte')
    find_product = filters.CharFilter(field_name='product_positions__product__title', lookup_expr='icontains')

    class Meta:
        model = Order
        fields = ('customer', 'created_at', )