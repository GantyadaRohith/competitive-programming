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
    cnt = 0
    s = {}
    for i in arr:
        if i&1:
            s[1] = s.get(1,0) + 1
        else:
            diff = i//2
            if diff&1:
                s[4] = s.get(4,0) + 1
            else:
                s[2] = s.get(2,0) + 1
    print(max(s.values()))