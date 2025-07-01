from django.db import models
from django.contrib.auth.models import User
class KapitalBank(models.Model):
    STATUS_CHOICES = [
    ("active", "Active"),
    ("inactive", "Inactive"),
    ("blocked", "Blocked"),
    ("expired", "Expired"),
    ("pending", "Pending"),
    ("closed", "Closed"),
]

    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='kapitalbank_users')
    bank = models.CharField(max_length=25)
    card_type = models.CharField(max_length=20)
    provider = models.CharField(max_length=30)
    card_number = models.CharField(max_length=16)
    expiry_month = models.IntegerField(default=0)
    expiry_year = models.IntegerField(default=0)
    cvv = models.IntegerField(default=1)
    currency = models.CharField(max_length=30)
    balance = models.DecimalField(max_digits=20, decimal_places=2)
    iban = models.CharField(max_length=34)
    account_type = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=16, choices=STATUS_CHOICES)
    loan_amount = models.DecimalField(max_digits=20, decimal_places=1)
    loan_term = models.IntegerField(default=0)
    interest_rate = models.DecimalField(max_digits=20, decimal_places=2)
    monthly_payment = models.DateTimeField(auto_now_add=True)
    transaction_type = models.CharField(max_length=30)
    transaction_amount = models.DecimalField(max_digits=30, decimal_places=3)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='kapitalbank_receivers')
    timestamp = models.DecimalField(max_digits=20, decimal_places=2)
    description = models.CharField(max_length=100)
    phone = models.CharField(max_length=30)
    fin_code = models.CharField(max_length=10)
    address = models.CharField(max_length=30)
    birth_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user