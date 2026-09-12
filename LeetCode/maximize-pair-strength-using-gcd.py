class Solution:
    def maxPairStrength(self, nums: list[int]) -> int:
        maxi = -float('inf')
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                maxi = max(maxi,((nums[i]*nums[j])//math.gcd(nums[i],nums[j])**2))
        return maxi
        