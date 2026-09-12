class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        c = 0
        a = x^y
        while a>0:
            a = a&(a-1)
            c+=1
        return c