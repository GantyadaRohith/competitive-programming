import sys
input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def invr():
    return(map(int,input().split()))
def inlt():
    return(list(map(int,input().split())))

t = inp()
for _ in range(t):
    n,k = invr()
    arr = inlt()
    a = {}
    a[k] = 0
    for i in arr:
        a[i] = a.get(i,0)+1
    if a[k] >= 1:
        print("YES")
    else:
        print("NO")