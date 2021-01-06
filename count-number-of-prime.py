n=int(input("Enter a number:"))
total = 0
while(n>0):
    digit =n%10
    total = total + digit
    n=n//10
    if(digit % 2) ==0:
        print(f'{digit} is not  a prime number')
    else:
        print(f'{digit} is  a prime number')
