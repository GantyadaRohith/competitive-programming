# 🟠 find-first-and-last-position-of-element-in-sorted-array — Find First and Last Position of Element in Sorted Array

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) &nbsp;|&nbsp; **Solved:** 2026-07-13

---

## 📝 Summary

Given a sorted array, find the first and last occurrence of a target value.

## 🔍 Key Observation

Use two passes to find the first and last occurrence of the target value efficiently.

## ⚙️ Algorithm

1. Iterate through the array to find the first occurrence of the target value.
2. If the target is found, continue iterating from the end of the array to find the last occurrence.
3. If the target is not found, return [-1, -1].

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to the two passes through the array.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`binary search` `two pointers` `sorted array`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        out = []
        for i in range(len(nums)):
            if nums[i] == target:
                out.append(i)
                break
        if not out:
            out.append(-1)
        for i in range(len(nums)-1,0,-1):
            if nums[i] == target:
                out.append(i)
                break
        if len(out) != 2:
            out.append(out[0])
        return out
        
```

</details>
