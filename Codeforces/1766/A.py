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
    if n<=9:
        print(n)
    else:
        l = len(str(n))
        msb = int(str(n)[0])
        cnt = 0
        while l>0:
            if l == 1:
                cnt+=msb
                break
            l-=1
            cnt+=9
        print(cnt)

