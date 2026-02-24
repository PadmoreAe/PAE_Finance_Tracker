from django.contrib import admin
from .models import Expense, Income
from accounts.models import Account

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('name', 'provider', 'account_type', 'balance', 'user')
    list_filter = ('account_type', 'provider')
    search_fields = ('name', 'provider')

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('description', 'amount', 'category', 'account', 'date')
    list_filter = ('category', 'date')

@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('source', 'amount', 'account', 'date')