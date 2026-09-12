st = input()
lower = upper = 0
for i in st:
    if i.islower():
        lower+=1
    else:
        upper+=1
if lower < upper:
    print(st.upper())
else:
    print(st.lower())