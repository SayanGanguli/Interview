value = int(input("Enter the value: "))
num = list(str(value))
size = len(num)
max_digit = 0
min_digit = 0
for val in range(size):
    if value % 10 > max_digit:
        max_digit = value % 10
        value = value // 10
    else:
        value = value // 10

print (max_digit)