# 🟠 unique-middle-element — Unique Middle Element

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/unique-middle-element/) &nbsp;|&nbsp; **Solved:** 2026-07-18

---

## 📝 Summary

Given an array of integers, determine if the middle element is unique.

## 🔍 Key Observation

The middle element is unique if it does not appear elsewhere in the array.

## ⚙️ Algorithm

1. Check if the array has only one element. If so, it is unique by default.
2. Calculate the middle index of the array.
3. Compare the middle element with all other elements in the array.
4. If any element matches the middle element and is not the middle element itself, return False.
5. If no such element is found, return True.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to the single pass through the array to find the middle element and another pass to check for uniqueness.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`python` `array` `unique` `middle`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        mid = n//2
        temp = nums[mid]
        for i in range(n):
            if nums[i] == temp and i!=mid :
                return False
        return True
```

</details>
