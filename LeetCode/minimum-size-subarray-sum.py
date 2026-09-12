class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        minlr = float('inf')
        s = 0
        left = 0
        for r in range(n):
            s += nums[r]
            while(s>=target):
                minlr = min(minlr,r - left + 1)
                s-=nums[left]
                left+=1
        if minlr == float('inf'):
            return 0
        else:
            return minlr
