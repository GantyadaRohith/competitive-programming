# 🟠 find-all-numbers-disappeared-in-an-array-ii — Find All Numbers Disappeared in an Array II

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array-ii/) &nbsp;|&nbsp; **Solved:** 2026-08-23

---

## 📝 Summary

Given an array of integers, find all numbers in the range [lower, upper] that are missing from the array.

## 🔍 Key Observation

The solution leverages the properties of sets to efficiently find missing numbers.

## ⚙️ Algorithm

1. Convert the input list to a set to remove duplicates and allow for O(1) average time complexity for lookups.
2. Iterate through the range [lower, upper] and collect numbers not found in the set.
3. Group consecutive missing numbers into sublists and return the list of sublists.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to the single pass through the input list and the range [lower, upper].` | `O(n) for the set and the output list.` |

## 🏷️ Tags

`python` `set` `range` `missing numbers`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def findDisappearedNumbers(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:
        out = []
        nums = set(nums)
        for i in range(lower,upper+1):
            if i not in nums:
                out.append(i)
        start = None
        end = None
        o = []
        for i in out:
            if start is None:
                start = i
                end = i
            elif end+1 == i:
                end = i
            else:
                o.append([start,end])
                start = end = i
        if start is not None:
            o.append([start,end])
        return o
            
```

</details>
