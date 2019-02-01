test = raw_input("enter the word")
s = ""
for i in range(0, len(test)):
    if test[i].islower():
        s = s+test[i].upper()
    elif test[i].isupper():
        s = s+(test[i].lower())
    else:
        s = s+test[i]
print(s)
print(test.swapcase())

