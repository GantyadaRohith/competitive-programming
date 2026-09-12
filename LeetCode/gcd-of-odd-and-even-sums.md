# 🟠 gcd-of-odd-and-even-sums — GCD of Odd and Even Sums

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/gcd-of-odd-and-even-sums/) &nbsp;|&nbsp; **Solved:** 2026-07-15

---

## 📝 Summary

Given an integer n, return the greatest common divisor (GCD) of the sums of odd and even numbers up to n.

## 🔍 Key Observation

The sums of odd and even numbers up to n are both multiples of n.

## ⚙️ Algorithm

The sums of odd numbers up to n are n * (n + 1) / 2, and the sums of even numbers up to n are n * n / 2. Since both sums are multiples of n, their GCD is n.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(1) due to constant-time calculations.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`gcd` `odd` `even` `sums`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        return n
```

</details>
