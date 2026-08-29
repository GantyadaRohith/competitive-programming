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

l,b = invr()
i = 1
while l*(3) <= b*(2):
    l = l*3
    b = b*2
    i+=1
print(i)
