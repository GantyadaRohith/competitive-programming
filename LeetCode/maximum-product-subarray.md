# 🟠 maximum-product-subarray — Maximum Product Subarray

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/maximum-product-subarray/) &nbsp;|&nbsp; **Solved:** 2025-12-10

---

## 📝 Summary

Find the maximum product of a contiguous subarray within an array of integers.

## 🔍 Key Observation

The solution uses a two-pass approach to keep track of the maximum and minimum products at each step, considering the possibility of negative numbers flipping the sign of the product.

## ⚙️ Algorithm

The algorithm iterates through the array twice: once from left to right and once from right to left. It maintains two variables, `l` and `r`, to store the maximum and minimum products up to the current position. This is necessary because a negative number can turn a small negative product into a large positive product. The maximum product is updated at each step by comparing the current product with the maximum product found so far.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n), where n is the length of the array. The algorithm makes a single pass through the array twice.` | `O(1) auxiliary space. The algorithm uses a constant amount of extra space regardless of the input size.` |

## 🏷️ Tags

`medium` `array` `dynamic-programming`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_pro = -float('inf')
        l = r = 1
        for i in range(len(nums)):
            if(l==0):
                l = nums[i]
            else:
                l*=nums[i]
            max_pro = max(l,max_pro)
        for i in range(len(nums)-1,-1,-1):
            if(r==0):
                r = nums[i]
            else:
                r*=nums[i]
            max_pro = max(r,max_pro)   
        return max_pro
```

</details>
