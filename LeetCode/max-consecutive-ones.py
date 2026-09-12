class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = 0
        tempcnt = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                tempcnt +=1
            else:
                tempcnt = 0
            cnt = max(tempcnt,cnt)
        return cnt