# 🟠 smallest-stable-index-i — Smallest Stable Index I

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/smallest-stable-index-i/) &nbsp;|&nbsp; **Solved:** 2026-09-04

---

## 📝 Summary

Find the smallest index `i` in an array `nums` such that the maximum element in the prefix `nums[0...i]` minus the minimum element in the suffix `nums[i...n-1]` is less than or equal to a given integer `k`. Return -1 if no such index exists.

## 🔍 Key Observation

The problem explicitly asks for the *smallest* stable index, making a direct linear scan from index `0` upwards the most intuitive approach. The first index `i` found to satisfy the given condition will be the correct answer.

## ⚙️ Algorithm

**Brute-force linear scan. Iterate through each possible index `i` from `0` to `n-1`. In each iteration, compute the maximum value within the prefix `nums[0...i]` and the minimum value within the suffix `nums[i...n-1]`. If their difference is less than or equal to `k`, return `i`. If the loop completes without finding such an index, return -1.**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n^2)` | `O(n)` |

## 🏷️ Tags

`arrays` `bruteforce` `linear scan` `simulation`

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
