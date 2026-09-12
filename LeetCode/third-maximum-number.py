class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        s = set(nums)
        s = list(s)
        s.sort()
        print(s)
        print(len(s))
        if len(s)<=2:
            return max(nums)
        else:
            return s[-3]
        