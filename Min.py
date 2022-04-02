value = int(input("Enter the value: "))

min = 9

while value > 0:
    digit = value % 10
    if min > digit:
        min = digit
    value = value // 10

print("Smallest Digit is : ", min)
