from django.contrib import admin
from shop.models import Customer, Product, ProductReview, Order, ProductsForOrder, ProductsCollection


class CustomerAdmin(admin.ModelAdmin):
    pass


class ProductAdmin(admin.ModelAdmin):
    pass


class ProductReviewAdmin(admin.ModelAdmin):
    pass


class OrderAdmin(admin.ModelAdmin):
    pass


class ProductsForOrderAdmin(admin.ModelAdmin):
    pass


class ProductsCollectionAdmin(admin.ModelAdmin):
    pass


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(ProductsForOrder, ProductsForOrderAdmin)
admin.site.register(ProductsCollection, ProductsCollectionAdmin)