from abc import ABC

from rest_framework import serializers
from ..models import Product, ProductReview, Order, ProductsCollection, ProductsForOrder


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductReview
        fields = '__all__'


class ProductsForOrderSerializer(serializers.Serializer):
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), source="product.id")
    order_id = serializers.PrimaryKeyRelatedField(queryset=Order.objects.all(), source="order.id")
    title = serializers.CharField(source='product.title', read_only=True)
    amount = serializers.IntegerField(min_value=1, max_value=10)
    sum_price = serializers.DecimalField(max_digits=9, decimal_places=2)

    class Meta:
        model = ProductsForOrder
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    positions = ProductsForOrderSerializer(many=True, required=True)

    class Meta:
        model = Order
        fields = '__all__'


class ProductsCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductsCollection
        fields = '__all__'
