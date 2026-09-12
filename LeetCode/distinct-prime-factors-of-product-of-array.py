class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        n = 1
        factors = set()
        for i in nums:
            while i % 2 == 0:
                factors.add(2)
                i //= 2  
            for j in range(3, int(math.sqrt(i)) + 1, 2):
                while i % j == 0:
                    if i not in factors:
                        factors.add(j)
                    i //= j
            if i > 2:
                factors.add(i)
        return len(set(factors))