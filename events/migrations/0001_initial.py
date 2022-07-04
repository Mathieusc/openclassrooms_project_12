# Generated by Django 4.0.4 on 2022-05-20 13:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contracts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'Not attributed'), (2, 'In progress'), (3, 'Ended')], default=1)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('attendees', models.IntegerField(blank=True, null=True)),
                ('event_dates', models.DateTimeField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, max_length=2000)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='client_event', to='clients.client')),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='contract_event', to='contracts.contract')),
                ('support_contact', models.ForeignKey(blank=True, limit_choices_to={'role': 2}, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='support', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
