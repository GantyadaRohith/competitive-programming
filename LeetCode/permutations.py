class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def perm(nums,seen):
            if len(seen) == len(nums):
                res.append(seen[:])
                return
            for i in nums:
                if i not in seen:
                    seen.append(i)
                    perm(nums,seen)
                    seen.pop()
        perm(nums,[])
        return res