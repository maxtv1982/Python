from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from ..models import Product, ProductReview, Order, ProductsCollection, ProductsForOrder


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductReview
        fields = '__all__'

    def validate(self, attrs):
        score = attrs.get('score')
        if score not in (1, 2, 3, 4, 5):
            raise ValidationError({"score": " оценка от 1 до 5 "})
        return attrs


class ProductsForOrderSerializer(serializers.Serializer):
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), source="product.id")
    title = serializers.CharField(source='product.title', read_only=True)
    price = serializers.DecimalField(max_digits=9, decimal_places=2, source='product.price', read_only=True)
    amount = serializers.IntegerField(min_value=1, max_value=10)


class OrderSerializer(serializers.ModelSerializer):
    product_positions = ProductsForOrderSerializer(many=True, required=True)
    final_price = serializers.DecimalField(required=False, max_digits=9, decimal_places=2)

    class Meta:
        model = Order
        exclude = ('positions',)

    def validate(self, attrs):
        positions = attrs.get('product_positions')
        print(positions)
        if not positions:
            raise ValidationError({"product_positions": "Не указан спис товаров"})

        positions_ids_set = {product["product"]["id"].id for product in positions}
        if len(positions_ids_set) != len(positions):
            raise ValidationError({"product_positions": "В заказе содержатся дубли"})
        return attrs

    def create(self, validated_data):
        products = validated_data.pop("product_positions")
        order = super().create(validated_data)

        for product in products:
            order.final_price += product["amount"] * product["product"]["id"].price
            ProductsForOrder.objects.create(
                amount=product["amount"],
                product=product["product"]["id"],
                order=order, )
        Order.objects.filter(id=order.id).update(final_price=order.final_price)
        return order


class ProductsCollectionSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = ProductsCollection
        fields = ('header', 'content', 'products',)
