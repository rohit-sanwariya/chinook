from rest_framework.generics import ListAPIView
from django.db.models import Sum, F
from sales.models import Customer
from .serializers import CustomerSpendingSerializer


class CustomerSpendingReport(ListAPIView):

    serializer_class = CustomerSpendingSerializer

    def get_queryset(self):
        return (
            Customer.objects
            .annotate(
                total_spent=Sum(
                    F("invoices__lines__quantity") *
                    F("invoices__lines__unit_price")
                )
            )
            .order_by("-total_spent")
        )