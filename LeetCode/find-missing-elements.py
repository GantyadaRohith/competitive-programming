class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        mi,ma=min(nums),max(nums)
        out = []
        for i in range(mi,ma+1):
            if i not in nums:
                out.append(i)
        return out
            