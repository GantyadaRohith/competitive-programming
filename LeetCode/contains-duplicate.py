class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dp = {}

        for i in nums:
            if i in dp:
                return True
            dp[i] = 1
        return False