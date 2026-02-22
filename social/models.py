from django.db import models
from django.conf import settings

class TransactionRequest(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('ACCEPTED', 'Accepted'),
        ('DECLINED', 'Declined'),
    ]

    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sent_requests')
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='received_requests')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(help_text="What is this request for?")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    chat_note = models.TextField(blank=True, null=True, help_text="Short chat message back and forth")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Request from {self.sender} to {self.receiver} for {self.amount}"