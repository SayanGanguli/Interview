invalue = int(input("Enter the number: "))
value = invalue
size = len(list(str(value)))
#print(size)
max = 0
for v in range(size):
    if value % 10 > max:
        max = value % 10
        value = value // 10
    else:
        value = value // 10

min = 9

while invalue > 0:
    digit = invalue % 10
    if min > digit:
        min = digit
    invalue = invalue // 10

print (max , min )