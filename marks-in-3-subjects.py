marks1 = float(input("Enter marks in 1st subject: "))
marks2 = float(input("Enter marks in 2nd subject: "))
marks3 = float(input("Enter marks in 3rd subject: "))

sum = marks1 + marks2 + marks3
avg = sum / 3
print(f'Total Marks {sum}')
print(f'Average is {avg}')
if avg < 35:
    print(f'Grade is C')
elif avg > 35 and avg < 60:
    print(f'Grade is B')
else:
    print(f'Grade is A')
   