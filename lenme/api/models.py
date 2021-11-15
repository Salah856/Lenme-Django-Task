from django.db import models
from datetime import datetime as dt

# Create your models here.

LOAN_STATUS = (
    ('Requested', 'Requested'),
    ('Funded', 'Funded'),
    ('Completed', 'Completed'),
)


class Investor(models.Model):
    investorname = models.CharField(max_length=100)
    investor_id = models.CharField(primary_key=True, max_length=100)
    balance = models.IntegerField(default=0)


class Borrower(models.Model):
    borrowername = models.CharField(max_length=100)
    borrower_id = models.CharField(primary_key=True, max_length=100)


class Loan(models.Model):
    loan_id = models.CharField(primary_key=True, max_length=100)
    loan_amount = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    loan_period = models.DateTimeField(
            dt.now() + dt.timedelta(days=180)
        )  # 6 months
    loan_status = models.CharField(choices=LOAN_STATUS, max_length=100)
    borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE)
    investor = models.ForeignKey(Investor, on_delete=models.CASCADE)


