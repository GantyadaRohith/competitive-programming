n,k = map(int,input().split())
a = list(map(int,input().split()))
d = {}
count = 0
for i in a:
    d[i] = d.get(i,0) + 1
d = list(d.items())
d.sort(key = lambda x:x[0],reverse= True)
i = 0
while count<k and i <= len(d)-1:
    if d[i][0] == 0:
        break
    count+=d[i][1]
    i+=1
print(count)