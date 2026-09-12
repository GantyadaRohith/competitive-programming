class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [0]*len(nums)
        post = [0]*len(nums)
        post[len(nums)-1] = nums[len(nums)-1]
        pre[0] = nums[0]
        for i in range(1,len(nums)):
            pre[i] = nums[i]*pre[i-1]
        for i in range(len(nums)-2,-1,-1):
            print(i)
            post[i] = nums[i] * post[i+1]
        res = [0]*len(nums)
        for i in range(1,len(nums)-1):
            res[i] = pre[i-1]*post[i+1]
        res[0] = post[1]
        res[len(nums)-1] = pre[len(nums)-2]
        return res