class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        out = []
        maxi = 0
        ans = 0
        for num in nums:
            digits = [int(d) for d in str(num)]
            ma = max(digits)
            mi = min(digits)
            maxi = max(maxi,ma-mi)
        for num in nums:
            digits = [int(d) for d in str(num)]
            ma = max(digits)
            mi = min(digits)
            if ma-mi == maxi:
                ans+=num
        return ans