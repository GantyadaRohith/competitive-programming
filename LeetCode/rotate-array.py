class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n     # handle large k

        # reverse helper
        def rev(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        # reverse whole array
        rev(0, n-1)
        # reverse first k
        rev(0, k-1)
        # reverse rest
        rev(k, n-1)
