class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        s = set(nums)
        maxnum = max(nums)
        ans = 0

        for g in range(1, maxnum + 1):
            cur_gcd = 0
            for multiple in range(g, maxnum + 1, g):
                if multiple in s:
                    cur_gcd = math.gcd(cur_gcd, multiple // g)
                    if cur_gcd == 1:
                        ans += 1
                        break

        return ans