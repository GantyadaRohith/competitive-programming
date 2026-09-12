class Solution(object):
    def uniqueXorTriplets(self, nums):
        n=len(nums)
        a=set()
        if n < 3:
            return len(set(nums))
        MAXX = 2048
        m = list(set(nums))
        for i in m:
            for j in m:
                a.add(i^j)
        b=set()
        for i in a:
            for j in m:
                b.add(i^j)
        return len(b)