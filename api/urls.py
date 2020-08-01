from rest_framework.routers import DefaultRouter
from .views import TransactionsViewSet

router = DefaultRouter()
router.register(r'transactions', TransactionsViewSet, basename='transactions')
urlpatterns = router.urls