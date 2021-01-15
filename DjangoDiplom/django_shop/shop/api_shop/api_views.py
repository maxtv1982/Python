from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, permissions
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .filters import ProductFilter, ProductReviewFilter, OrderFilter

from ..models import Product, ProductReview, Order, ProductsForOrder, ProductsCollection
from .serializers import ProductSerializer, ProductReviewSerializer, OrderSerializer, ProductsCollectionSerializer, \
    ProductsForOrderSerializer


class IsCustomerOrAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        return obj.customer == request.user


class AdminPermission(permissions.BasePermission):
    message = 'Adding products only by admin.'

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS or request.user.is_staff:
            return True


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filter_class = ProductFilter
    ordering_fields = ['price']
    ordering = ['title']
    permission_classes = [AdminPermission, ]


class ProductReviewViewSet(ModelViewSet):
    queryset = ProductReview.objects.select_related('product').all()
    serializer_class = ProductReviewSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filter_class = ProductReviewFilter
    ordering_fields = ['customer', 'created_at', 'product']
    permission_classes = [IsCustomerOrAdmin, ]

    def create(self, request):
        serializer = ProductReviewSerializer(data=request.data)
        request.data['customer'] = request.user.id

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.order_by('created_at').all()
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filter_class = OrderFilter
    ordering_fields = ['status', 'customer', 'final_price', 'created_at', 'updated_at', 'product_positions']
    permission_classes = [IsCustomerOrAdmin, ]

    def get_queryset(self):
        if not self.request.user.is_staff:
            queryset = Order.objects.filter(customer=self.request.user.id)
        else:
            queryset = Order.objects.all()
        return queryset


class ProductsCollectionViewSet(ModelViewSet):
    queryset = ProductsCollection.objects.all()
    serializer_class = ProductsCollectionSerializer
    permission_classes = [AdminPermission, ]


class ProductsForOrderViewSet(ModelViewSet):
    queryset = ProductsForOrder.objects.all()
    serializer_class = ProductsForOrderSerializer
