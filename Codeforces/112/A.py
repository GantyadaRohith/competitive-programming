str1 = input()
str2 = input()
a = {}
j = 0
for i in 'abcdefghijklmnopqrstuvwxyz':
    a[i] = j
    j+=1
str1 = str1.lower()
str2 = str2.lower()
if str1 == str2:
    print(0)
else:
    for i in range(len(str1)):
        if a[str1[i]] > a[str2[i]]:
            print(1)
            break
        elif a[str1[i]] < a[str2[i]]:
            print(-1)
            break
