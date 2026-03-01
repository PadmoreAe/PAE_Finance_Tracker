from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Expense
from .serializers import ExpenseSerializer
from .permissions import IsOwner # this imports the owner rule
from django.db.models import Sum
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from accounts.models import Account
from rest_framework import viewsets
from .models import Expense, Income
from .serializers import ExpenseSerializer, IncomeSerializer
from decimal import Decimal


class ExpenseViewSet(viewsets.ModelViewSet):
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    #serializer class
    queryset = Expense.objects.all().order_by('-date')
    serializer_class = ExpenseSerializer

    def get_queryset(self): # set user sees only their acc
        return Expense.objects.filter(user=self.request.user).order_by('-date')
    def perform_create(self, serializer):
        # This automatically attaches the logged-in user to the new expense.
        serializer.save(user=self.request.user)

#serializer class
class IncomeViewSet(viewsets.ModelViewSet):
    queryset = Income.objects.all().order_by('-date')
    serializer_class = IncomeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Income.objects.filter(user=self.request.user).order_by('-date')
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TotalBalanceView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # All accounts belonging ONLY to the logged-in user
        user_accounts = Account.objects.filter(user=request.user)
        # Adds up all the balances
        total = user_accounts.aggregate(Sum('balance'))['balance__sum'] or 0.00
        # Counts how many pockets (accounts) you have
        account_count = user_accounts.count()

        return Response({
            "username": request.user.username,
            "total_balance": total,
            "currency": request.user.preferred_currency,
            "number_of_accounts": account_count
        })

#Report view 
class ReportView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        # Actual balance from accounts (source of truth)
        user_accounts = Account.objects.filter(user=user)
        total_balance = user_accounts.aggregate(
            Sum('balance'))['balance__sum'] or Decimal('0.00')

        # Total income from records
        total_income = Income.objects.filter(user=user).aggregate(
            Sum('amount'))['amount__sum'] or Decimal('0.00')

        # Total expenses from records
        total_expenses = Expense.objects.filter(user=user).aggregate(
            Sum('amount'))['amount__sum'] or Decimal('0.00')

        # Expenses broken down by category
        expenses_by_category = Expense.objects.filter(user=user).values(
            'category').annotate(total=Sum('amount')).order_by('-total')

        # Income broken down by source
        income_by_source = Income.objects.filter(user=user).values(
            'source').annotate(total=Sum('amount')).order_by('-total')

        return Response({
            "actual_balance": total_balance,        # real money in accounts
            "total_income_recorded": total_income,  # income history
            "total_expenses_recorded": total_expenses, # expense history
            "net_from_transactions": total_income - total_expenses, # history based
            "expenses_by_category": list(expenses_by_category),
            "income_by_source": list(income_by_source),
        })