input_text = "When you click Online Video, you can paste in the embed code for the video you want to add. You can also type a keyword to search online for the video that best fits your document."
input_text = input_text.replace(".", "")
input_text = input_text.split()

output = []
for word in input_text:
    if word not in output:
        output.append(word)

for i in range(0, len(output)):
    print(output[i], "==", input_text.count(output[i]))
