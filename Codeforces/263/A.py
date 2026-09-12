a = []
for i in range(5):
    a.append(list(map(int,input().split())))
i,j = 0,0
for k in range(5):
    for l in range(5):
        if a[k][l] == 1:
            i,j = k,l
            break
cnt = abs(i-2)+abs(j-2)
print(cnt) 