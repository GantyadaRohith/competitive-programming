class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for i in range(n,101):
            pro = 1
            for j in str(i):
                pro*=int(j)
            if pro%t == 0:
                return i