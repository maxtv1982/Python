from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .filters import ProductFilter, ProductReviewFilter, OrderFilter

from ..models import Product, ProductReview, Order, ProductsForOrder, ProductsCollection
from .serializers import ProductSerializer, ProductReviewSerializer, OrderSerializer, ProductsCollectionSerializer, \
    ProductsForOrderSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filter_class = ProductFilter
    ordering_fields = ['price']
    ordering = ['title']


class ProductReviewViewSet(ModelViewSet):
    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filter_class = ProductReviewFilter
    ordering_fields = ['customer', 'created_at', 'product']


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.order_by('created_at').all()
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filter_class = OrderFilter
    ordering_fields = ['status', 'final_price', 'created_at', 'updated_at', 'positions__product']


class ProductsCollectionViewSet(ModelViewSet):
    queryset = ProductsCollection.objects.all()
    serializer_class = ProductsCollectionSerializer


class ProductsForOrderViewSet(ModelViewSet):
    queryset = ProductsForOrder.objects.all()
    serializer_class = ProductsForOrderSerializer
