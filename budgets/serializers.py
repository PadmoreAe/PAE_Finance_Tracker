from rest_framework import serializers
from .models import Budget, SavingsGoal

class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = ['id', 'category', 'limit', 'period', 'created_at']
        read_only_fields = ['id', 'created_at']


class SavingsGoalSerializer(serializers.ModelSerializer):
    progress_percentage = serializers.ReadOnlyField()

    class Meta:
        model = SavingsGoal
        fields = ['id', 'account', 'name', 'target_amount', 'saved_amount', 'deadline', 'progress_percentage', 'created_at']
        read_only_fields = ['id', 'created_at']