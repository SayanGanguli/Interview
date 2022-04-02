text = input("Enter text= ")
str =""
for i in text:
    str = i + str

if str==text:
    print("Palindrome")
else:
    print("Not Palindrome")
