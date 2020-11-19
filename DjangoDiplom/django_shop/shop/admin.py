from django.contrib import admin
from .models import Product, ProductReview, Order, ProductsForOrder, ProductsCollection


class CollectionInline(admin.TabularInline):
    model = ProductsCollection.products.through
    extra = 1


class ProductsForOrderInline(admin.TabularInline):
    model = ProductsForOrder
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    inlines = [CollectionInline, ProductsForOrderInline, ]
    list_display = ('title', 'created_at')


class ProductReviewAdmin(admin.ModelAdmin):
    pass


class OrderAdmin(admin.ModelAdmin):
    inlines = [ProductsForOrderInline, ]


# class ProductsForOrderAdmin(admin.ModelAdmin):
#     pass


class ProductsCollectionAdmin(admin.ModelAdmin):
    inlines = [CollectionInline, ]
    exclude = ('products',)
    list_display = ('header', 'created_at')


# admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)
admin.site.register(Order, OrderAdmin)
# admin.site.register(ProductsForOrder, ProductsForOrderAdmin)
admin.site.register(ProductsCollection, ProductsCollectionAdmin)