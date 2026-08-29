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
    a = []
    for _ in range(10):
        a.append(input())
    pts = 0
    for i in range(10):
        for j in range(10): 
            layer = min(i, j, 9-i, 9-j) + 1
            if a[i][j] == 'X':
                pts+=layer
    print(pts)
