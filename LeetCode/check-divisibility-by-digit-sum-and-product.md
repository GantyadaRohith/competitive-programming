# 🟠 check-divisibility-by-digit-sum-and-product — Check Divisibility by Digit Sum and Product

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/check-divisibility-by-digit-sum-and-product/) &nbsp;|&nbsp; **Solved:** 2026-08-22

---

## 📝 Summary

The problem asks to check if a given integer `n` is divisible by the sum of its digit sum and its digit product.

## 🔍 Key Observation

The solution directly implements the problem statement by extracting digits to calculate their sum and product, then performing a modular arithmetic check.

## ⚙️ Algorithm

**Digit extraction and direct calculation**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(log N)` | `O(log N)` |

## 🏷️ Tags

`math` `digits` `arithmetic` `simulation`

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
