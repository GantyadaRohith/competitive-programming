class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        bestSum = nums[0]+nums[1]+nums[2]

        for i in range(n - 2):
            l, r = i + 1, n - 1

            while l < r:
                total = nums[i] + nums[l] + nums[r]

                if abs(total - target) < abs(bestSum - target):
                    bestSum = total
                if total < target:
                    l += 1
                elif total > target:
                    r -= 1
                else :
                    return total
        return bestSum