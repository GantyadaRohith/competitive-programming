t = int(input())
for _ in range(t):
    n = int(input())
    cnt = 0
    if n>0 and n<10:
        print(1)
        print(n)
    else:
        s = str(n)
        for i in range(len(s)):
            if s[i]!= '0':
                cnt+=1
        print(cnt)
        for i in range(len(s)):
            if s[i]!= '0':
                print(s[i]+'0'*(len(s)-int(i)-1),end = " ")
        print()
    