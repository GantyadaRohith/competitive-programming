word = input()
if word[0].islower():
    print(word[0].upper()+word[1:])
else:
    print(word)