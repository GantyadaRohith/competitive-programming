m,n = map(int,input().split())
s = '#'*n
t1 = '.'*(n-1)+'#'
t2 = '#'+'.'*(n-1)
f = 0
for i in range(m):
    if i%2 == 0:
        print(s)
    elif f == 0:
        f = 1
        print(t1)
    else:
        f = 0
        print(t2)