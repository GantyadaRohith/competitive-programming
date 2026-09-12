# 🟠 check-divisibility-by-digit-sum-and-product — Check Divisibility by Digit Sum and Product

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/check-divisibility-by-digit-sum-and-product/) &nbsp;|&nbsp; **Solved:** 2026-08-22

---

## 📝 Summary

Given an integer n, determine if it is divisible by the sum of its digits plus the product of its digits.

## 🔍 Key Observation

The solution involves calculating the sum and product of the digits of n and checking if n is divisible by their sum plus product.

## ⚙️ Algorithm

1. Convert the integer n to a string to easily iterate over each digit.
2. Initialize variables `ds` (digit sum) and `pro` (digit product) to 0 and 1 respectively.
3. Iterate over each character in the string representation of n, convert it to an integer, and update `ds` and `pro` accordingly.
4. Check if n is divisible by `ds + pro` and return the result.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(d) where d is the number of digits in n, as we iterate over each digit once.` | `O(1) auxiliary space, as we only use a fixed amount of extra space regardless of the input size.` |

## 🏷️ Tags

`easy` `math` `digit manipulation`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def checkDivisibility(self, n: int) -> bool:
        ds = 0
        pro = 1
        for i in str(n):
            ds+=int(i)
            pro*=int(i)
        if n%(ds+pro) == 0:
            return True
        else:
            return False    
```

</details>
