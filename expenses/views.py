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


class ExpenseViewSet(viewsets.ModelViewSet):
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    #serializer class
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

    def get_queryset(self): # set user sees only their acc
        return Expense.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # This automatically attaches the logged-in user to the new expense.
        serializer.save(user=self.request.user)

#serializer class
class IncomeViewSet(viewsets.ModelViewSet):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer


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