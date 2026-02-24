from django.db import models
from django.conf import settings
from accounts.models import Account


class Expense(models.Model):
    CATEGORY_CHOICES = [('FOOD', 'Food'),('TRANSPORT', 'Transport'),('RENT', 'Rent'),('MOMO_FEE', 'Momo Fees'),
        ('OTHER', 'Other'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='expenses')
    account = models.ForeignKey('accounts.Account', on_delete=models.CASCADE, related_name='expense_records')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='OTHER')
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Logic: expense automatically subtracts from the account
        if not self.pk:
            self.account.balance -= self.amount
            self.account.save()
        super().save(*args, **kwargs)
    # def __str__(self):
    #     return f"{self.description} - {self.amount}"


#Transaction type
class Income(models.Model):
    INCOME_SOURCES = [('SALARY', 'Salary'),('GIFT', 'Gift'),('BUSINESS', 'Business/Profit'),('OTHER', 'Other'),]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    account = models.ForeignKey('accounts.Account', on_delete=models.CASCADE, related_name='income_records' )
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    source = models.CharField(max_length=20, choices=INCOME_SOURCES, default='OTHER')
    description = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # The Magic Rule: Add money to the account balance when income is created
        if not self.pk:
            self.account.balance += self.amount
            self.account.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.source}: +{self.amount} to {self.account.name}"


# is_pending_detail = models.BooleanField(default=False)