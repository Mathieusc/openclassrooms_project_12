from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    MANAGEMENT = 1
    SUPPORT = 2
    SALES = 3

    USER_ROLE = ((MANAGEMENT, "management"), (SUPPORT, "support"), (SALES, "sales"))

    role = models.PositiveIntegerField(
        choices=USER_ROLE, verbose_name="role", blank=True, null=True
    )

    def __str__(self):
        return f"User: {self.email} | Role: {self.role}"
