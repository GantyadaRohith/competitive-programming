a = int(input())
for _ in range(a):
    n = int(input())
    s = list(map(int,input().split()))
    cnt = 0
    temp = 0
    for i in range(n):
        if s[i] == 0:
            temp+=1
        elif temp>0 and s[i] == 1:
            cnt = max(cnt,temp)
            temp = 0
        cnt = max(cnt,temp)
    print(cnt)
