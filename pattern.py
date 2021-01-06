rows = int(input("Enter the number of rows: "))  
  

for i in range(1, rows+1):  
     
    for j in range(1, i + 1):  
        print(j, end=' ')  
    print("")

#2nd Pattern
n = int(input("Enter the number of rows: "))  
num = 1 
for row in range(1,n+1):
    for col in range(1,row+1): 
        print(num, end=" ")    
        num = num +1
    print()

#3rd Pattern
n = int(input("Enter the number of rows: "))  
num = 1 
for row in range(1,n+1):
    for col in range(1,n+1): 
        print(num, end=" ")    
        num = num +1
    print()

#4th Pattern
rows = int(input("Enter the number of rows: "))  
  

for i in range(rows,1,-1):  
     
    for j in range(1,i):  
        print(j, end=' ')  
    print("")

#5th pattern
for row in range(7):
    for col in range(5):
        if col==2 or ((row==0 or row==6) and col!=2):
            print("*",end="")
        else:
            print(end=" ")
    print("")

#6th pattern
for row in range(7):
    for col in range(5):
        if ((col==0 or col==4) and row!=0) or ((row==0 or row==3) and (col>0 and col<4)) :
            print("@", end= "")
        else:
            print(end=" ")
    print("")

#7th pattern
rows = int(input("Enter the number of rows: "))  
  

for i in range(rows,1,-1):  
     
    for j in range(1,i):  
        print(j, end=' ')  
    print("")

#8th pattern
n = int(input("Enter the number of rows: "))  
num = 19 
for row in range(1,n+1):
    for col in range(1,n+1): 
        print(num, end=" ")    
        
    print()