def check_investor_balance(investor_id, loan):
    investor = Investor.objects.get(pk=investor_id)
    return investor.balance > loan.loan_amount + loan.lenme_fee
