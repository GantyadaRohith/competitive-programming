class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        mid = n//2
        temp = nums[mid]
        for i in range(n):
            if nums[i] == temp and i!=mid :
                return False
        return True