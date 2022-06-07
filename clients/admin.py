from django.contrib import admin
from clients.models import Client

# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    model = Client

    list_display = [
        "sales_contact",
        "company_name",
        "first_name",
        "last_name",
        "email",
        "mobile",
    ]
    list_filter = ["sales_contact", "company_name"]
    search_fields = ["first_name", "last_name"]
