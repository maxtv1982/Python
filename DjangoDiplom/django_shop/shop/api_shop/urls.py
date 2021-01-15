from rest_framework.routers import SimpleRouter
from .api_views import ProductViewSet, ProductReviewViewSet, OrderViewSet, ProductsCollectionViewSet

router = SimpleRouter()
router.register("products", ProductViewSet, basename="products")
router.register("product-reviews", ProductReviewViewSet, basename="product-reviews")
router.register("orders", OrderViewSet, basename="orders")
router.register("product-collections", ProductsCollectionViewSet, basename="product-collections")


urlpatterns = [] + router.urls