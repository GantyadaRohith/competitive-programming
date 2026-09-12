import sys
input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))

t = inp()
for _ in range(t):
    n = inp()
    a = inlt()
    x = a[0]
    for i in range(1,n):
        x^=a[i]
    if n&1:
        print(x)
    else:
        if x == 0:
            print(0)
        else:
            print(-1)

