from django.db import models
from authentication.models import User
from contracts.models import Contract
from clients.models import Client


class Event(models.Model):
    CHOICES_STATUS = ((1, "Not attributed"), (2, "In progress"), (3, "Ended"))
    status = models.PositiveSmallIntegerField(choices=CHOICES_STATUS, default=1)
    contract = models.ForeignKey(
        to=Contract, on_delete=models.RESTRICT, related_name="contract_event"
    )
    client = models.ForeignKey(
        to=Client, on_delete=models.RESTRICT, related_name="client_event"
    )
    support_contact = models.ForeignKey(
        to=User,
        on_delete=models.RESTRICT,
        null=True,
        blank=True,
        limit_choices_to={"role": 2},
        related_name="support",
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    attendees = models.IntegerField(blank=True, null=True)
    event_dates = models.DateTimeField(blank=True, null=True)
    notes = models.TextField(max_length=2000)

    def __str__(self):
        return f"Contract: {self.contract} | Status: {self.status} | Support Staff: {self.support_contact}"
