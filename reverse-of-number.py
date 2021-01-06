n=int(input("Enter number: "))
revrs = 0
while(n>0):
    digit = n%10
    revrs=revrs*10+digit
    n=n//10
print(f'Reverse is: {revrs}')