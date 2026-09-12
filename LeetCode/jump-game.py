class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        table = [False] * n
        table[-1] = True

        for i in range(n-2, -1, -1):
            far = min(i + nums[i], n - 1)
            for j in range(i + 1, far + 1):
                if table[j]:
                    table[i] = True
                    break

        return table[0]