class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        i = 1
        nums = set(nums)
        while True:
            if k*i in nums:
                i+=1
                continue
            else:
                return k*i