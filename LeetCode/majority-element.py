class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        limit = n//2
        x = {}
        res = nums[0]
        for i in nums:
            x[i] = x.get(i,0) + 1
            if x[i] > limit:
                res = i
        return res