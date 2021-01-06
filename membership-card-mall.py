bill_amnt = input('Enter the bill amount: ')
membership_card = input('Do you have a membership card? ')[0]

if membership_card == 'y' or 'Y':
    disc = float(bill_amnt) * 0.1 
    net_bill = float (bill_amnt) - disc
    print (f'Thank you! Your total bill amount is Rs {bill_amnt}, discount is Rs {disc} and net amount payable is Rs {net_bill}.')
else:
    disc = float(bill_amnt) * 0.03 
    net_bill = float (bill_amnt) - disc
    print (f'Thank you! Your total bill amount is Rs {bill_amnt}, discount is Rs {disc} and net amount payable is Rs {net_bill}.')