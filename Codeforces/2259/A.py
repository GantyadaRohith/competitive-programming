import sys
input = sys.stdin.readline
 
############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().strip())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))
 
t = inp()
for _ in range(t):
    n,k = invr()
    arr = inlt()
    cnt = 0
    for i in range(0, n, k):
        x = arr[i:i+k]
        if 0 not in x:
            cnt+=1
    print(cnt)