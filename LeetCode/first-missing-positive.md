# 🟠 first-missing-positive — First Missing Positive

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/first-missing-positive/) &nbsp;|&nbsp; **Solved:** 2026-02-25

---

## 📝 Summary

Find the smallest positive integer that does not appear in the given list of integers.

## 🔍 Key Observation

The key insight is to use a set to mark the presence of numbers and then find the first missing positive integer.

## ⚙️ Algorithm

1. Convert the list to a set for O(1) average time complexity lookups.
2. Iterate through the range from 1 to the length of the list plus one.
3. Return the first number not found in the set.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to the set operations and the linear scan.` | `O(n) for the set.` |

## 🏷️ Tags

`python` `set` `linear scan`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        s = set(nums)
        for i in range(1,len(nums)+2):
            if i not in s:
                return i
```

</details>
