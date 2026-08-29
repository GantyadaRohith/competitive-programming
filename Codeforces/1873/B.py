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
    prod = 1
    c = 0
    for i in a:
        if i == min(a) and c == 0:
            i+=1
            c+=1
        prod*=i
    print(prod)