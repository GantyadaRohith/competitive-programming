# 🟠 find-minimum-in-rotated-sorted-array — Find Minimum in Rotated Sorted Array

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) &nbsp;|&nbsp; **Solved:** 2025-12-11

---

## 📝 Summary

Find the minimum element in a rotated sorted array.

## 🔍 Key Observation

The array is rotated, so the minimum element is in the unsorted part.

## ⚙️ Algorithm

Use binary search to find the minimum element. Compare the middle element with the leftmost element. If the middle element is greater than the leftmost, the minimum is in the right half; otherwise, it is in the left half.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(log n) due to binary search.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`binary search` `sorted array` `rotation`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            m = (l + r) // 2

            if nums[m] >= nums[l]:
                if nums[l] > nums[r]:
                    l = m + 1
                else:
                    r = m -1
            elif nums[m] < nums[r]:
                r = m
        return nums[m]
```

</details>
