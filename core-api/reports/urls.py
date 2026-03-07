from django.urls import path
from .views import CustomerSpendingReport

urlpatterns = [
    path("customer-spending/", CustomerSpendingReport.as_view()),
]