# 🟠 powx-n — Pow(x, n)

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/powx-n/) &nbsp;|&nbsp; **Solved:** 2026-08-08

---

## 📝 Summary

Calculate x raised to the power of n efficiently.

## 🔍 Key Observation

The solution leverages Python's built-in exponentiation operator `**` for efficient computation.

## ⚙️ Algorithm

The algorithm uses the built-in exponentiation operator to compute `x` raised to the power of `n`. This approach is efficient and concise.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(1) due to the constant time complexity of the exponentiation operator.` | `O(1) auxiliary space as no additional data structures are used.` |

## 🏷️ Tags

`python` `built-in` `exponentiation`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x**n
```

</details>
