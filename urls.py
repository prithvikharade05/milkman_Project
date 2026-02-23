from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('customers', CustomerViewSet)
router.register('categories', CategoryViewSet)
router.register('products', ProductViewSet)
router.register('subscriptions', SubscriptionViewSet)

urlpatterns = router.urls