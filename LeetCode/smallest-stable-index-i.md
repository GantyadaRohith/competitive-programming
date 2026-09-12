# 🟠 smallest-stable-index-i — Smallest Stable Index I

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/smallest-stable-index-i/) &nbsp;|&nbsp; **Solved:** 2026-09-04

---

## 📝 Summary

Find the smallest index in the array such that the maximum difference between the maximum and minimum values in the subarray ending at that index is less than or equal to k.

## 🔍 Key Observation

The solution uses a sliding window approach to efficiently find the smallest stable index.

## ⚙️ Algorithm

The algorithm iterates through the array while maintaining a window of elements ending at the current index. It checks if the difference between the maximum and minimum values in this window is less than or equal to k. If so, it returns the current index. If no such index is found, it returns -1.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to a single pass through the array.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`sliding window` `array` `minimum` `maximum`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        for i in range(len(nums)):
            if (max(nums[:i+1]) - min(nums[i:])) <= k:
                return i
            if i == len(nums)-1:
                return -1
```

</details>
