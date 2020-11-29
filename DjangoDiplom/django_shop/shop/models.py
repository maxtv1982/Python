from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class OrderStatus(models.TextChoices):
    NEW = "NEW", "Новый заказ"
    IN_PROGRESS = "IN_PROGRESS", "Оформление заказа"
    DONE = " DONE", "заказ выполнен"


class Product(models.Model):
    title = models.CharField(max_length=50, verbose_name='наименование')
    description = models.TextField(blank=True, verbose_name='описание')
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='цена')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='дата обновления')

    def __str__(self):
        return self.title


class ProductReview(models.Model):
    customer = models.OneToOneField(User, verbose_name='покупатель', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name='продукт', on_delete=models.CASCADE)
    review = models.TextField(verbose_name='отзыв')
    score = models.PositiveSmallIntegerField(verbose_name='оценка')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='дата обновления')

    def __str__(self):
        return "отзыв : {}".format(self.product.title)


class Order(models.Model):
    customer = models.ForeignKey(User, verbose_name='покупатель', on_delete=models.CASCADE)
    positions = models.ManyToManyField(Product, through='ProductsForOrder')
    status = models.TextField(default='New', choices=OrderStatus.choices, verbose_name='статус')
    final_price = models.DecimalField(blank=True, max_digits=9, decimal_places=2, default=0, verbose_name='итоговая стоимость')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='дата обновления')

    def __str__(self):
        return "заказ № {} для покупателя {}".format(self.id, self.customer)


class ProductsForOrder(models.Model):
    product = models.ForeignKey(Product, verbose_name='продукт', on_delete=models.CASCADE)
    order = models.ForeignKey(Order, related_name="product_positions", verbose_name='заказ', on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=1, verbose_name='количество единиц товара')
    sum_price = models.DecimalField(blank=True, max_digits=9, decimal_places=2, verbose_name='цена за товары')

    def save(self, *args, **kwargs):
        self.sum_price = self.amount * self.product.price
        super().save(*args, **kwargs)


class ProductsCollection(models.Model):
    header = models.CharField(max_length=50, verbose_name='заголовок')
    content = models.TextField(null=True, verbose_name='содержание')
    products = models.ManyToManyField(Product, related_name='collections')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='дата обновления')

    def __str__(self):
        return self.header
