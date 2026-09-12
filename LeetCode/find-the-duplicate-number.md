# 🟠 find-the-duplicate-number — Find the Duplicate Number

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/find-the-duplicate-number/) &nbsp;|&nbsp; **Solved:** 2026-08-14

---

## 📝 Summary

Given an array of integers where each integer appears at most once except for one that appears twice, find the duplicate number.

## 🔍 Key Observation

The duplicate number can be found by using a set to track seen numbers and identifying the first duplicate encountered.

## ⚙️ Algorithm

1. Initialize an empty set `s` to keep track of seen numbers.
2. Iterate through each number `i` in the input list `nums`:
   - If `i` is not in `s`, add it to `s`.
   - If `i` is already in `s`, return `i` as it is the duplicate number.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to a single pass through the list.` | `O(n) auxiliary space for the set.` |

## 🏷️ Tags

`short` `lowercase` `find` `duplicate`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s = set()
        for i in nums:
            if i not in s:
                s.add(i)
            else:
                return i
        
```

</details>
