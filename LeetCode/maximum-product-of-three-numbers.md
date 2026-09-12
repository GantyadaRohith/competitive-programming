# 🟠 maximum-product-of-three-numbers — Maximum Product of Three Numbers

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/maximum-product-of-three-numbers/) &nbsp;|&nbsp; **Solved:** 2026-07-26

---

## 📝 Summary

Given an array of integers, find the maximum product of three numbers.

## 🔍 Key Observation

The maximum product can be either the product of the three largest numbers or the product of the two smallest numbers (which could be negative) and the largest number.

## ⚙️ Algorithm

1. Sort the array in ascending order.
2. The maximum product can be either the product of the last three elements (largest numbers) or the product of the first two elements (smallest numbers) and the last element (largest number).
3. Return the maximum of these two products.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log n) due to sorting.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`short` `lowercase` `sort` `max`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        return max((nums[-1]*nums[-2]*nums[-3]),(nums[0]*nums[1]*nums[-1]))
```

</details>
