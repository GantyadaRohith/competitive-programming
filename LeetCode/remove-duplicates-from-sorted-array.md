# 🟠 remove-duplicates-from-sorted-array — Remove Duplicates from Sorted Array

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) &nbsp;|&nbsp; **Solved:** 2025-11-21

---

## 📝 Summary

Remove duplicates from a sorted array in-place, returning the length of the new array.

## 🔍 Key Observation

Use two pointers to track the position of the last unique element and iterate through the array.

## ⚙️ Algorithm

Initialize a slow pointer `i` to 0. Iterate through the array with a fast pointer `j`. If the current element is different from the element at `i`, increment `i` and update `nums[i]` with the current element. Return `i + 1` as the length of the new array.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to a single pass through the array.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`python` `two-pointer` `in-place`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0

        i = 0  # slow pointer

        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]

        return i + 1

```

</details>
