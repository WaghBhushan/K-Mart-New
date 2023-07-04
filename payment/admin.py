from django.contrib import admin
from .models import PaymentOrder


class PaymentOrderAdmin(admin.ModelAdmin):
    list_display = ['order','transaction_id','status']
    search_fields = ['order']


admin.site.register(PaymentOrder,PaymentOrderAdmin)
