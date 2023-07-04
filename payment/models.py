from django.db import models
from order.models import Order


class PaymentOrder(models.Model):
    STATUS_CHOICE =(
        ('Pending','Pending'),
        ('Inprogress','Inprogress'),
        ('Completed','Completed'),
        ('Rejected','Rejected'),
    )
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    transaction_id = models.CharField(max_length=55)
    status = models.CharField(max_length=55 , choices=STATUS_CHOICE) 

    def __str__(self):
        return str(self.order)

