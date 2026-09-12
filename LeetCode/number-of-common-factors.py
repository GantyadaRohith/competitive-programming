class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        s = set()
        for i in range(1,1001):
            if a%i == 0 and b%i == 0:
                s.add(i)
        return len(s)