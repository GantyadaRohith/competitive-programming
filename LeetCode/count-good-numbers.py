class Solution:
    def countGoodNumbers(self, n: int) -> int:
        even = (n+1)//2
        odd = n//2
        mod = 10**9+7
        def power(a,b):
            res = 1
            a%=mod
            while b>0:
                if b%2 == 1:
                    res = (res*a)%mod
                a = (a*a)%mod
                b//=2
            return res
        p1 = power(5,even)
        p2 = power(4,odd)
        return (p1*p2)%1000000007
