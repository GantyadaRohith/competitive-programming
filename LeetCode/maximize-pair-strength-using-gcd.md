# 🟠 maximize-pair-strength-using-gcd — Maximize Pair Strength Using GCD

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/maximize-pair-strength-using-gcd/) &nbsp;|&nbsp; **Solved:** 2026-08-02

---

## 📝 Summary

Given an array of integers, find the maximum product of a pair of numbers where the product is maximized by dividing by their greatest common divisor (GCD).

## 🔍 Key Observation

The key insight is to maximize the product by ensuring the GCD is minimized, as the GCD reduces the product.

## ⚙️ Algorithm

1. Initialize `maxi` to negative infinity to store the maximum product found.
2. Iterate over all pairs of numbers in the array.
3. For each pair, calculate the product of the numbers and divide it by their GCD squared.
4. Update `maxi` with the maximum value obtained from these calculations.
5. Return `maxi` as the result.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n^2) due to the nested loops over all pairs of numbers.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`medium` `math` `gcd` `pair`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def maxPairStrength(self, nums: list[int]) -> int:
        maxi = -float('inf')
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                maxi = max(maxi,((nums[i]*nums[j])//math.gcd(nums[i],nums[j])**2))
        return maxi
        
```

</details>
