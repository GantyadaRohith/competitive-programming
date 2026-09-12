class Solution:
    def findDisappearedNumbers(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:
        out = []
        nums = set(nums)
        for i in range(lower,upper+1):
            if i not in nums:
                out.append(i)
        start = None
        end = None
        o = []
        for i in out:
            if start is None:
                start = i
                end = i
            elif end+1 == i:
                end = i
            else:
                o.append([start,end])
                start = end = i
        if start is not None:
            o.append([start,end])
        return o
            