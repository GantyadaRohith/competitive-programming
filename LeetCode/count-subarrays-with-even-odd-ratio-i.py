class Solution:
    def countRatioSubarrays(self, nums: list[int], a: int, b: int) -> int:
        count = 0
        for i in range(len(nums)):
            oc,ec = 0,0
            for j in range(i,len(nums)):
                if nums[j]&1:
                    oc += 1
                else:
                    ec += 1
                if oc > 0 and (ec/oc) <= (a/b):
                    count+=1
        return count