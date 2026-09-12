class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_pro = -float('inf')
        l = r = 1
        for i in range(len(nums)):
            if(l==0):
                l = nums[i]
            else:
                l*=nums[i]
            max_pro = max(l,max_pro)
        for i in range(len(nums)-1,-1,-1):
            if(r==0):
                r = nums[i]
            else:
                r*=nums[i]
            max_pro = max(r,max_pro)   
        return max_pro