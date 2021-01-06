bill_amount = input('Enter the billing amount? ')

if float(bill_amount) > 6000 :
    net_billing_amount = float(bill_amount) - float(bill_amount) * 0.1
    print(f'Net billing amount is {net_billing_amount}')
else:
    print(f'Net billing amount is {bill_amount}')