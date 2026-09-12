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
    x = {-1:0,1:0}
    for i in a:
        x[i] += 1
    cnt = 0
    while x[-1]>x[1]:
           x[-1]-=1
           cnt+=1
           x[1]+=1
    if x[-1]&1:
        x[-1]-=1
        cnt+=1
    print(cnt)