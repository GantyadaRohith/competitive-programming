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
    arr = inlt()
    a = {}
    b = {}
    for i in range(n):
        a[arr[i]] = i
        b[arr[i]] = b.get(arr[i],0) + 1
    for i,j in b.items():
        if j == 1:
            print(a[i]+1)
            break
    
    