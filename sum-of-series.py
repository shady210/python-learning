num = int(input("Enter the number: "))
def sum(num): 
    x = 0
    for i in range(1, num+1): 
        x = x + 1/i; 
    return x; 
  

print("Sum is", sum(num)) 
