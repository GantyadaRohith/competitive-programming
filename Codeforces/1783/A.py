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
    ar1 = sorted(arr,reverse=True)
    if arr==ar1:
        print('NO')
    else:
        for i in range(1,n):
            if sum(ar1[:i]) == ar1[i]:
                ar1[i],ar1[-1] = ar1[-1],ar1[i]
        print("YES")
        print(*ar1)