class Solution:
    def checkDivisibility(self, n: int) -> bool:
        ds = 0
        pro = 1
        for i in str(n):
            ds+=int(i)
            pro*=int(i)
        if n%(ds+pro) == 0:
            return True
        else:
            return False    