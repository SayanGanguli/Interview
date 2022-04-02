text = "When you click Online Video you can paste in the embed code"
text = text.lower()

lt = {}

for i in text:
    if i in lt:
        lt[i] += 1
    else:
        lt[i] = 1

print(lt)
