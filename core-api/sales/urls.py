from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register("customers", CustomerViewSet)
router.register("invoices", InvoiceViewSet)
router.register("invoice-lines", InvoiceLineViewSet)

urlpatterns = router.urls