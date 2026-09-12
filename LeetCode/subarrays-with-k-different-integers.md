# 🟠 subarrays-with-k-different-integers — Subarrays with K Different Integers

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/subarrays-with-k-different-integers/) &nbsp;|&nbsp; **Solved:** 2025-12-10

---

## 📝 Summary

Given an array of integers and an integer k, find the number of subarrays with exactly k distinct integers.

## 🔍 Key Observation

Use a sliding window approach to count subarrays with at most k distinct integers and subtract the count with at most k-1 distinct integers.

## ⚙️ Algorithm

1. Initialize a frequency dictionary to keep track of the count of each integer in the current window.
2. Use two pointers, left and right, to represent the current window.
3. Expand the window by moving the right pointer and updating the frequency dictionary.
4. If the number of distinct integers exceeds k, shrink the window from the left by moving the left pointer and updating the frequency dictionary.
5. Count the number of valid subarrays by adding the length of the current window to the answer.
6. Return the total count of valid subarrays.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to a single pass through the array with two pointers.` | `O(n) for the frequency dictionary.` |

## 🏷️ Tags

`sliding window` `hash map` `subarrays`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.atMostK(nums, k) - self.atMostK(nums, k - 1)
    def atMostK(self, nums, k):
        freq = defaultdict(int)
        left = 0
        ans = 0

        for right in range(len(nums)):
            freq[nums[right]] += 1

            while len(freq) > k:
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1

            ans += right - left + 1
        
        return ans
```

</details>
