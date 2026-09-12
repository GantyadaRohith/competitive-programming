class Solution:

    def largestInteger(self, nums: List[int], k: int) -> int:
        freq = Counter()

        # Iterate through every contiguous subarray of size k
        for i in range(len(nums) - k + 1):
            window = nums[i : i + k]
            # Use set() to count an element at most once per window
            for num in set(window):
                freq[num] += 1

        # Find the maximum element that appeared in exactly one subarray of size k
        ans = -1
        for num, count in freq.items():
            if count == 1:
                ans = max(ans, num)

        return ans