word = input("Give me a text: ")

for i in word:
    if i.isupper():
        print(i.lower() , end="")
    else:
        print(i.upper() , end="")