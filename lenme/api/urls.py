from django.urls import path
from .views import request_loan, submit_loan_offer, accept_loan, complete_loan


urlpatterns = [
    path('request_loan/', request_loan, name='request_loan'),
    path('submit_loan_offer/', submit_loan_offer, name='submit_loan_offer'),
    path('accept_loan/', accept_loan, name='accept_loan'),
    path('complete_loan/', complete_loan, name='complete_loan'),
]
