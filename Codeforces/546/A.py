import sys
input = sys.stdin.readline
def invr():
    return(map(int,input().split()))

k,n,w = invr()
su = (w*(w+1))/2
to = su*k
if to >= n:
    print(int(to-n))
else:
    print(0)