from django.db import models
from .customer import Customer
from utils.constants.status import STATUS_PAYMENT

# Create your models here.


class Payment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    external_id = models.CharField(unique=True, max_length=60)
    total_amount = models.DecimalField(max_digits=20, decimal_places=10)
    status = models.PositiveSmallIntegerField(default=1,choices=STATUS_PAYMENT)
    paid_at = models.DateTimeField(auto_now=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f'{self.id} - {self.external_id} - {self.customer_id.external_id}'