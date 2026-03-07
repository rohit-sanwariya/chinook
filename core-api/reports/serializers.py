from rest_framework import serializers


class CustomerSpendingSerializer(serializers.Serializer):
    customer_id = serializers.IntegerField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    total_spent = serializers.DecimalField(max_digits=10, decimal_places=2)