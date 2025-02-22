
user_input = str(input("Enter a Phrase: "))
text = user_input.split()
a = " "
for i in text:
    a = a+str(i[0]).upper()
print(a)

# split() splits a sentence into individual words
# splitting a word to letters would require using list()