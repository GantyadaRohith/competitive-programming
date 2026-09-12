# 🟠 find-all-numbers-disappeared-in-an-array-ii — Find All Numbers Disappeared in an Array II

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array-ii/) &nbsp;|&nbsp; **Solved:** 2026-08-23

---

## 📝 Summary

Given an array of integers `nums` and a range `[lower, upper]`, find all numbers within that range that are not present in `nums`, and return them as a list of contiguous ranges.

## 🔍 Key Observation

Efficiently identify all missing numbers in the specified range using a hash set, then group these individual missing numbers into consecutive ranges.

## ⚙️ Algorithm

**Hash Set (for lookup) + Range Grouping**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(N + (upper - lower))` | `O(N + (upper - lower))` |

## 🏷️ Tags

`array` `set` `range` `missing numbers` `two pointers`

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
