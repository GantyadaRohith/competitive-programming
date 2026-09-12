class Solution:
    def removeElement(self, nums, val):
        i = 0  # slow pointer

        for j in range(len(nums)):  # fast pointer
            if nums[j] != val:      # keep only elements NOT equal to val
                nums[i] = nums[j]
                i += 1

        return i
