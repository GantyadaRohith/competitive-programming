class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        arr = []
        for i in range(0,len(nums),2):
            arr.append((nums[i],nums[i+1]))
        sum = 0
        for i in range(len(arr)):
            sum+=min(arr[i][0],arr[i][1])
        return sum