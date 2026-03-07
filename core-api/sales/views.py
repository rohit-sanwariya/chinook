from rest_framework.viewsets import ModelViewSet

from sales.models import Customer, Invoice, InvoiceLine
from sales.serializers import CustomerSerializer, InvoiceLineSerializer, InvoiceSerializer


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.select_related("support_rep").all()
    serializer_class = CustomerSerializer


class InvoiceViewSet(ModelViewSet):
    queryset = (
        Invoice.objects
        .select_related("customer")
        .prefetch_related("lines")
        .all()
    )
    serializer_class = InvoiceSerializer


class InvoiceLineViewSet(ModelViewSet):
    queryset = (
        InvoiceLine.objects
        .select_related("invoice", "track")
        .all()
    )
    serializer_class = InvoiceLineSerializer