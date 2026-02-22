from rest_framework import serializers
from .models import Expense

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        # These are the fields we want to show in the API
        fields = ['id', 'user', 'account', 'amount', 'description', 'category', 'date']
        read_only_fields = ['user', 'date']