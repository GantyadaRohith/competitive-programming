class Solution:
    def longestSubarray(self, nums: list[int], k: int) -> int:
        def p_f(n):
            factors = []
            d = 2
            while d*d <= n:
                if n%d == 0:
                    factors.append(d)
                    while n%d == 0:
                        n//=d
                d+=1
            if n > 1:
                factors.append(n)
            return factors
        a = {}
        for i in nums:
            a[i] = p_f(i)
        freq = {}
        dist = 0
        l = ans = 0
        for r in range(len(nums)):
            for x in a[nums[r]]:
                if freq.get(x,0) == 0:
                    dist+=1
                freq[x] = freq.get(x,0) + 1
            while dist > k:
                for p in a[nums[l]]:
                    freq[p]-=1
                    if freq[p] == 0:
                        dist-=1
                l+=1
            ans = max(ans,r-l+1)
        return ans
        