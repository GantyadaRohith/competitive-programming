n = int(input())
count = 0
le = len(str(n))
while n:
    i = n%10
    n//=10
    if i in {4,7}:
        count+=1
if count in {4,7}:
    print('YES')
else:
    print('NO')