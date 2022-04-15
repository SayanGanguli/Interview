import re
text = "bfbv9204hhvgdf645r74hv2098"

#Fetching only digit from a string
pattern1 = "\d+"
result1 = re.findall(pattern1, text)
res = re.split(pattern1, text)
print(result1)
print(res)

#Fetching only non-digit from a string
pattern2 = "\D+"
result2 = re.findall(pattern2, text)
print(result2)




