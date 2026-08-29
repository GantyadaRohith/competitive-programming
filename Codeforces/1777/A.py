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
    out = [arr[0]]
    cnt = 0
    for i in range(1,n):
        if (out[-1]&1 == 1 and arr[i]&1 == 1)or (out[-1]&1 == 0 and arr[i]&1 == 0):
            cnt+=1
            temp = out.pop()
            out.append(temp*arr[i])
        else:
            out.append(arr[i])
    print(cnt)