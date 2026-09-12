class Solution:
    def jump(self, nums: List[int]) -> int:
        jump = 0
        curend = 0
        far = 0
        for i in range(len(nums)-1):
            far = max(far,i+nums[i])
            if(i==curend):
                jump+=1
                curend = far
        return jump