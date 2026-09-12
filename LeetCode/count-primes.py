N = 5*10**6
p = [1]*(N+1)
p[0] = p[1] = 0
for i in range(2, N+1):
    if p[i]:
        for j in range(i*i, N+1, i):
            p[j] = 0
    p[i] += p[i-1]
class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0:
            return 0
        return p[n-1]