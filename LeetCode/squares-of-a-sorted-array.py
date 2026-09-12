class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums)-1
        k = len(nums)-1
        sqr = [-1]*(len(nums))
        while i <= j:
            if abs(nums[i]) < abs(nums[j]):
                sqr[k] = nums[j]*nums[j]
                j-=1
                k-=1
            else:
                sqr[k] = nums[i]*nums[i]
                i+=1
                k-=1
        return sqr