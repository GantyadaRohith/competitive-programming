# 🟠 distinct-prime-factors-of-product-of-array — Distinct Prime Factors of Product of Array

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/distinct-prime-factors-of-product-of-array/) &nbsp;|&nbsp; **Solved:** 2026-02-23

---

## 📝 Summary

Given an array of integers, find the number of distinct prime factors of their product.

## 🔍 Key Observation

The solution uses a set to store prime factors, ensuring uniqueness.

## ⚙️ Algorithm

The algorithm iterates through each number in the array, dividing it by 2 to handle even numbers, then checks for odd factors up to the square root of the number. If a number remains greater than 2 after processing, it is also a prime factor.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log n) due to the division by 2 and the loop through odd factors up to the square root of each number.` | `O(1) auxiliary space as the set of prime factors is stored in a set.` |

## 🏷️ Tags

`python` `prime factors` `set` `math`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        n = 1
        factors = set()
        for i in nums:
            while i % 2 == 0:
                factors.add(2)
                i //= 2  
            for j in range(3, int(math.sqrt(i)) + 1, 2):
                while i % j == 0:
                    if i not in factors:
                        factors.add(j)
                    i //= j
            if i > 2:
                factors.add(i)
        return len(set(factors))
```

</details>
