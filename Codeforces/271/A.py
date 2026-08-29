import sys
input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp():
    return(int(input()))

year = inp()
for i in range(year+1,9013):
    s = set()
    n = 0
    for j in str(i):
        if j not in s:
            s.add(j)
            n+=1
        else:
            break
    if n == 4:
        print(i)
        break