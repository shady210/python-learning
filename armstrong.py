num = int(input("Please Enter the Number to Check for Armstrong: "))

sum = 0
dig_time = 0
           
temp = num
while temp > 0:
           dig_time = dig_time + 1
           temp = temp // 10
temp = num
while temp > 0:
           rem = temp % 10
           sum = sum + (rem ** dig_time)
           temp //= 10
if num == sum:
           print(f"{num} is Armstrong Number.")
else:
           print(f"{num} is not a Armstrong Number.")
