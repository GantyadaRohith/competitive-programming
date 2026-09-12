class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        rate = 1
        l = 1
        hi = max(piles)
        while l<hi:
            rate = (hi+l)//2
            H = 0
            for i in piles:
                H += math.ceil(i/rate)
            if H<=h:
                hi = rate
            else:
                l = rate+1
        return l