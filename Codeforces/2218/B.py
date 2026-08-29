import sys
input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))

t = inp()
for _ in range(t):
    arr = inlt()
    arr.sort(reverse=True)
    s = arr[0]
    for i in range(1,len(arr)):
        s-=arr[i]
    print(s)