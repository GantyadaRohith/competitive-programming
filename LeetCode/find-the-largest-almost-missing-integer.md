# 🟠 find-the-largest-almost-missing-integer — Find the Largest Almost Missing Integer

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/find-the-largest-almost-missing-integer/) &nbsp;|&nbsp; **Solved:** 2026-08-18

---

## 📝 Summary

Given an array of integers and a positive integer k, find the largest integer that appears in exactly one contiguous subarray of size k.

## 🔍 Key Observation

The key insight is to use a sliding window approach to count the frequency of each integer in every subarray of size k.

## ⚙️ Algorithm

1. Initialize a frequency counter to keep track of the count of each integer in the current window of size k.
2. Iterate through the array, updating the frequency counter for each integer in the current window.
3. After processing each window, find the maximum integer that appears exactly once.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) where n is the length of the array, as each element is processed at most twice (once for each window it belongs to).` | `O(n) for the frequency counter, as it stores the count of each integer in the current window.` |

## 🏷️ Tags

`sliding window` `frequency counting` `array`

<details>
<summary>💻 View solution</summary>

```python
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
```

</details>
