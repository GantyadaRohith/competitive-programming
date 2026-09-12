n = int(input())
out = []
for i in range(n):
    s = input()
    n = len(s)
    if len(s)<=10:
        print(s)
    else:
        print(s[0]+str(len(s[1:n-1]))+s[-1])
