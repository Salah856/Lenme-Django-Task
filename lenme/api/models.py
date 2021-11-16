from django.db import models
from datetime import datetime as dt, timedelta

# Create your models here.

LOAN_STATUS = (
    ('Requested', 'Requested'),
    ('Offered', 'Offered'),
    ('Funded', 'Funded'),
    ('Paid', 'Paid'),
    ('Completed', 'Completed'),
)


class Investor(models.Model):
    investor_name = models.CharField(max_length=100, blank=True)
    investor_id = models.CharField(primary_key=True, max_length=100)
    balance = models.IntegerField(default=0, blank=True)


class Borrower(models.Model):
    borrower_name = models.CharField(max_length=100, blank=True)
    borrower_id = models.CharField(primary_key=True, max_length=100)


class Loan(models.Model):
    loan_id = models.CharField(primary_key=True, max_length=100)
    loan_amount = models.IntegerField(default=0, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    loan_period = models.DateTimeField(
            dt.now() + timedelta(days=180)
        )  # 6 months
    loan_status = models.CharField(
            choices=LOAN_STATUS,
            max_length=100,
            default=LOAN_STATUS[0][0]
        )
    annual_interest_rate = models.FloatField(default=0.15)
    lenme_fee = models.FloatField(default=3.0)
    # 3 dollars fee
    # to be added to loan amount

    borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE)
    investor = models.ForeignKey(Investor, on_delete=models.CASCADE)


