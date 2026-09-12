class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        def gcd(a,b):
            if b == 0:
                return a
            return gcd(b,a%b)
        if target<=x+y and target%gcd(x,y) == 0:
            return True
        return False