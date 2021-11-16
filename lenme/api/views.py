from django.shortcuts import render
from .models import Investor, Loan, Borrower
from django.http import JsonResponse


# Create your views here.


def request_loan(request):
    if request.method == 'POST':
        loan_amount = request.POST.get('loan_amount')
        lenme_fee = request.POST.get('lenme_fee')
        borrower_id = request.POST.get('borrower_id')
        # from frontend token
        investor_name = request.POST.get('investor_name')
        # user can select investor from dropdown list for example by name
        loan_period = request.POST.get('loan_period')

        investor_id = Investor.objects.get(investor_name=investor_name).pk

        all_filled = all(
            [loan_amount, lenme_fee, loan_period, investor_id, borrower_id]
        )

        if not all_filled:
            return JsonResponse(status=401, data={'message': 'fields missing'})

        loan = Loan(
            loan_amount=loan_amount,
            lenme_fee=lenme_fee,
            borrower_id=borrower_id,
            investor_id=investor_id,
            loan_period=loan_period,
            loan_status='Requested'
        )

        loan.save()

        return JsonResponse(status=201, data={'message': 'Loan request sent'})




def submit_loan_offer(request):
    if request.method == 'POST':
        investor_id = request.POST.get('investor_id')
        annual_interest_rate = request.POST.get('annual_interest_rate')
        loan_id = request.POST.get('loan_id')

        all_filled = all([investor_id, annual_interest_rate, loan_id])

        if not all_filled:
            return JsonResponse(data={'message': 'fields missing'}, status=401)

        loan = Loan.objects.get(pk=loan_id)

        loan.annual_interest_rate = annual_interest_rate
        loan.loan_status = 'Funded'
        loan.save()

        data = {'message': 'Loan offer submitted'}
        return JsonResponse(status=200, data=data)


