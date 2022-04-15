number = int(input("Enter Any Number: "))
input_num = number
num = []
while(number > 0):
    rem  = number % 10
    number  = number // 10
    num.append(rem)

sum = 0
for i in num :
    sum = sum + i ** 3

if sum == input_num:
    print ("It is Armstrong Number")
else:
    print("It is not Armstrong Number")
