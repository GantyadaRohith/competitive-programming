class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low,right = 0,len(nums)-1
        while low<right:
            mid = (low+right)//2
            if nums[mid] > nums[mid+1]:
                right = mid
            else:
                low = mid+1
        return low