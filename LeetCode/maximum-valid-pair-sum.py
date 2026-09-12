class Solution:
    def maxValidPairSum(self, nums: list[int], k: int) -> int:
        n = len(nums)
        maxi = 0
        pre = [-1]*(n)
        pre[0] = nums[0]
        print(pre)
        for i in range(1,n):
            pre[i] = max(pre[i-1],nums[i])
        for i in range(k,n):
            maxi = max(maxi,nums[i]+pre[i-k])
        return maxi
