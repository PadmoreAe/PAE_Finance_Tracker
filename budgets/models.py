from django.db import models
from django.conf import settings
from accounts.models import Account

class Budget(models.Model):
    CATEGORY_CHOICES = [
        ('FOOD', 'Food'),
        ('TRANSPORT', 'Transport'),
        ('RENT', 'Rent'),
        ('MOMO_FEE', 'Momo Fees'),
        ('OTHER', 'Other'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='budgets')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    limit = models.DecimalField(max_digits=12, decimal_places=2, help_text="Max spending allowed")
    period = models.CharField(max_length=10, choices=[('DAILY','Daily'),('WEEKLY','Weekly'),('MONTHLY','Monthly')], default='MONTHLY')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.category} budget: {self.limit}"


class SavingsGoal(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='savings_goals')
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='savings_goals')
    name = models.CharField(max_length=100, help_text="e.g. New Car, Emergency Fund")
    target_amount = models.DecimalField(max_digits=12, decimal_places=2)
    saved_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    deadline = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def progress_percentage(self):
        if self.target_amount == 0:
            return 0
        return round((self.saved_amount / self.target_amount) * 100, 2)

    def __str__(self):
        return f"{self.name} - {self.progress_percentage}% complete"