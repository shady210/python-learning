n=int(input("Enter a number:"))
total = 0
while(n):
    digit =n%10
    total = total + digit
    n=n//10
    print(f'{digit + 1}', end=" ")