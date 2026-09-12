# 🟠 check-if-array-is-sorted-and-rotated — Check if Array Is Sorted and Rotated

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/) &nbsp;|&nbsp; **Solved:** 2025-12-10

---

## 📝 Summary

Determine if an array is sorted and rotated.

## 🔍 Key Observation

The array is sorted and rotated if it has at most one element out of order.

## ⚙️ Algorithm

Iterate through the array and count the number of times an element is greater than the next element (considering the array as circular). If the count is more than one, return False; otherwise, return True.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to a single pass through the array.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`array` `rotation` `check`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0
        n = len(nums)

        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                count += 1

        return count <= 1

```

</details>
