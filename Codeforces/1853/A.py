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
    mini = 10**9+1
    for i in range(1,len(arr)):
        if mini > (arr[i]-arr[i-1]):
            mini = arr[i]-arr[i-1]
    if mini>=0:
        print((mini//2)+1)
    else:
        print(0)