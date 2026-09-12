class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        a = []
        for num in nums:
            if nums[abs(num)-1] < 0:
                a.append(abs(num))
            else:
                nums[abs(num)-1] *= -1
        return a