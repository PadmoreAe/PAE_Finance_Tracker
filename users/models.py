from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Custom fields for currency
    preferred_currency = models.CharField(max_length=3, default='GHS')
    language = models.CharField(max_length=10, default='en')

    def __str__(self):
        return self.username