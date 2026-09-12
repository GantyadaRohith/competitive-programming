n = int(input())
total = 0
maxi = -float('inf')
for _ in range(n):
    out,ini = map(int,input().split())
    total = total-out+ini
    maxi = max(maxi,total)
print(maxi)