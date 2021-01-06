
name = input('Enter the emplyee name? ')
mobile_number =  input('Enter the mobile number? ')
age = input('Enter the age? ')

if int(age) > 18:
    print (f'“Congratulations {name} for your successful registration.”')
else:
    print(f'"“Sorry! You need to be at least 18 years old to get membership.”')