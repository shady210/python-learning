n = int(input("Enter the number: "))
def fib(n):

    a = 0
    b = 1

    for i in range(2,n):
        c = a + b
        a = b
        b = c
        print(a+b, end=" ")
fib(n)