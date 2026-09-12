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

t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    f =  0
    if n % 2 == 0 or k % 2 == 1:
            print("YES")
    else:
            print("NO")