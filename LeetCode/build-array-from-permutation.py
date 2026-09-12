class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = [0]*(len(nums))
        j = 0 
        for i in nums:
            ans[j] = nums[i]
            j+=1
        return ans