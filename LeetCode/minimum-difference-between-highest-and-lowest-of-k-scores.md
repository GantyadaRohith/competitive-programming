# 🟠 minimum-difference-between-highest-and-lowest-of-k-scores — Minimum Difference Between Highest and Lowest of K Scores

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/) &nbsp;|&nbsp; **Solved:** 2025-11-20

---

## 📝 Summary

Given an array of integers and a positive integer k, find the minimum difference between the highest and lowest scores in any subarray of length k.

## 🔍 Key Observation

Sorting the array allows for efficient finding of the minimum difference by comparing adjacent elements.

## ⚙️ Algorithm

1. Sort the array of scores.
2. Initialize a variable `best` to infinity.
3. Iterate through the sorted array, comparing the difference between the k-th element and the (k-1)-th element.
4. Update `best` if the current difference is smaller.
5. Return `best` as the minimum difference.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log n) due to sorting.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`sort` `min` `difference` `subarray`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k <= 1 or n <= 1:
            return 0
        if k > n:
            return 0
    
        nums.sort()
        best = float('inf')
        for i in range(0, n - k + 1):
            diff = nums[i + k - 1] - nums[i]
            if diff < best:
                best = diff
        return best


```

</details>
