class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        result = [-1]*len(nums)
        N = 2*len(nums) - 1
        for i in range(N):
            i = i%len(nums)
            while stack and nums[stack[-1]] < nums[i]:
                p_i = stack.pop()
                result[p_i] = nums[i]        
            stack.append(i)
        return result
