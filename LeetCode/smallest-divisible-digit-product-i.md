# 🟠 smallest-divisible-digit-product-i — Smallest Divisible Digit Product I

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/smallest-divisible-digit-product-i/) &nbsp;|&nbsp; **Solved:** 2026-08-07

---

## 📝 Summary

Find the smallest positive integer with exactly n digits whose digits' product is divisible by t.

## 🔍 Key Observation

The solution iterates through numbers starting from n to 100, checking if the product of its digits is divisible by t.

## ⚙️ Algorithm

1. Iterate through numbers from n to 100.
2. For each number, calculate the product of its digits.
3. Check if the product is divisible by t.
4. Return the first number that satisfies the condition.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log n) due to sorting the digits of each number.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`short` `lowercase` `digit` `product` `divisible`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for i in range(n,101):
            pro = 1
            for j in str(i):
                pro*=int(j)
            if pro%t == 0:
                return i
```

</details>
