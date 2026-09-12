class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k <= 1 or n <= 1:
            return 0
        if k > n:
            return 0
    
        nums.sort()
        best = float('inf')
        for i in range(0, n - k + 1):
            diff = nums[i + k - 1] - nums[i]
            if diff < best:
                best = diff
        return best

