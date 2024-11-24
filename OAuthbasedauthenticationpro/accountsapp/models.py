from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Add extra fields if needed
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username
