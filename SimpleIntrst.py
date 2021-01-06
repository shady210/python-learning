2

principle = input('Enter the principle? ') 
year = input('Enter the year? ')
rate_of_interest = input('Enter the rate  of interest? ')

simple_interest = (float(principle) * float(rate_of_interest) * float(year))/100
print(f'Simple Interest is {simple_interest}')