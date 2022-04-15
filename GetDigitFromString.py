text = "bfbv9204hhvgdf645r74hv2098"

digit_list = []
for i in text:
    # print(i, end=" ")
    if i.isdigit():
        i = int(i)
        digit_list.append(i)

sum = 0
for k in digit_list:
    sum = sum + k

print(sum)




