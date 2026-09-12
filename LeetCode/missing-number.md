# 🟠 missing-number — Missing Number

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/missing-number/) &nbsp;|&nbsp; **Solved:** 2026-08-09

---

## 📝 Summary

Given a list of unique integers from 0 to n, find the missing number.

## 🔍 Key Observation

The missing number is the difference between the sum of the first n natural numbers and the sum of the given list.

## ⚙️ Algorithm

1. Sort the list of numbers.
2. Calculate the sum of the first n natural numbers using the formula n*(n+1)/2.
3. Calculate the sum of the numbers in the list.
4. Return the difference between the sum of the first n natural numbers and the sum of the list.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log n) due to sorting.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`short` `lowercase` `sort` `sum`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)+1):
            if i not in nums:
                return i
```

</details>
