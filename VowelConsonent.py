text = "how are you"
stext = text.replace(" ","")
vowels_c = 0
vowels =""
cons_c = 0
cons = ""
for t in stext:
    #print(t, end="&")
    if t == 'a' or t=='e' or t=='i' or t=='o' or t=='u':
        vowels_c = vowels_c + 1
        vowels = vowels +t
    else:
        cons_c = cons_c + 1
        cons = cons + t
print (vowels)
print(vowels_c)
print(cons)
print(cons_c)
