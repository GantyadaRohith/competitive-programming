class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        out = []
        for i in range(len(nums)):
            if nums[i] == target:
                out.append(i)
                break
        if not out:
            out.append(-1)
        for i in range(len(nums)-1,0,-1):
            if nums[i] == target:
                out.append(i)
                break
        if len(out) != 2:
            out.append(out[0])
        return out
        