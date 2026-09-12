# 🟠 maximum-product-of-two-elements-in-an-array — Maximum Product of Two Elements in an Array

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/) &nbsp;|&nbsp; **Solved:** 2026-07-27

---

## 📝 Summary

Find the maximum product of two distinct elements in an array.

## 🔍 Key Observation

The maximum product is achieved by multiplying the two largest numbers in the array.

## ⚙️ Algorithm

1. Sort the array in ascending order.
2. Calculate the product of the two largest numbers.
3. Calculate the product of the two smallest numbers (which could be negative, potentially yielding a larger product).
4. Return the maximum of these two products.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log n) due to sorting.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`sort` `two-pointers` `max-product`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        return max((nums[-1]-1)*(nums[-2]-1),(nums[0]-1)*(nums[1]-1))
```

</details>
