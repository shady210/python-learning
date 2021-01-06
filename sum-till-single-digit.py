n=int(input("Enter a number:"))
while (n > 9):
    sum = 0
  
    while n > 0:
        digit =n%10
        sum = sum + digit
        n=n//10
    n=sum

print(f'The total sum of digits is: {sum}')