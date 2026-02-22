from django.db import models
from django.conf import settings

class Account(models.Model):
    # The types account
    ACCOUNT_TYPES = [
        ('BANK', 'Bank Account'),
        ('MOMO', 'Mobile Money'),
        ('SUSU', 'Susu/Savings Group'),
        ('CASH', 'Physical Cash'),
        ('OTHER', 'Other'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='finance_accounts')
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, help_text="e.g. GCB Current Account")
    institution_name = models.CharField(max_length=100, blank=True, null=True, help_text="Specific Bank or Provider name")
    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPES, default='CASH')
    provider = models.CharField(max_length=50, help_text="e.g., MTN, Telecel, GCB, Ecobank")
    created_at = models.DateTimeField(auto_now_add=True)

    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    currency = models.CharField(max_length=3, default='GHS')

    def __str__(self):
        return f"{self.name} ({self.account_type}) - {self.balance} {self.currency}"
