# 🟠 remove-element — Remove Element

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/remove-element/) &nbsp;|&nbsp; **Solved:** 2025-11-21

---

## 📝 Summary

Remove all instances of a given value from an array and return the new length of the array.

## 🔍 Key Observation

Use two pointers to efficiently remove elements.

## ⚙️ Algorithm

Initialize a slow pointer `i` to track the position where the next non-target element should be placed. Iterate through the array with a fast pointer `j`. If the element at `j` is not equal to the target value, move it to the position at `i` and increment `i`. The final value of `i` represents the new length of the array without the target value.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to a single pass through the array.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`easy` `array` `two-pointer`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def removeElement(self, nums, val):
        i = 0  # slow pointer

        for j in range(len(nums)):  # fast pointer
            if nums[j] != val:      # keep only elements NOT equal to val
                nums[i] = nums[j]
                i += 1

        return i

```

</details>
