from rest_framework import serializers
from .models import Employee





class EmployeeSerializer(serializers.ModelSerializer):

    manager = serializers.StringRelatedField(source="reports_to", read_only=True)

    class Meta:
        model = Employee
        fields = "__all__"