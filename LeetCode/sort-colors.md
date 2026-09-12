# 🟠 sort-colors — Sort Colors

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/sort-colors/) &nbsp;|&nbsp; **Solved:** 2025-12-10

---

## 📝 Summary

Sort an array of integers containing only 0s, 1s, and 2s in-place.

## 🔍 Key Observation

The problem can be solved using the Dutch National Flag algorithm, which sorts the array in O(n) time with O(1) auxiliary space.

## ⚙️ Algorithm

1. Initialize three pointers: low = 0, mid = 0, high = n-1.
2. Traverse the array with the mid pointer:
   - If nums[mid] is 0, swap nums[mid] with nums[low] and increment both low and mid.
   - If nums[mid] is 1, increment mid.
   - If nums[mid] is 2, swap nums[mid] with nums[high] and decrement high.
3. Continue this process until mid exceeds high.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to a single pass through the array.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`sort` `in-place` `dutch-national-flag`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
```

</details>
