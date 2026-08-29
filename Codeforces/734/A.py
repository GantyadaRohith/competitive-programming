n = int(input())
st = input()
a = b = 0
for i in st:
    if i == 'A':
        a+=1
    else:
        b+=1
if a == b:
    print("Friendship")
elif a>b:
    print("Anton")
else:
    print("Danik")