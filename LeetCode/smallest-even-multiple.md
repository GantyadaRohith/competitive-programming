# 🟠 smallest-even-multiple — Smallest Even Multiple

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/smallest-even-multiple/) &nbsp;|&nbsp; **Solved:** 2026-07-25

---

## 📝 Summary

Find the smallest even multiple of a given integer.

## 🔍 Key Observation

The smallest even multiple of any integer is the integer itself if it is even, or twice the integer if it is odd.

## ⚙️ Algorithm

The solution checks if the input number `n` is even. If it is, the number is returned as the smallest even multiple. If `n` is odd, the solution returns `n * 2`, which is the smallest even multiple.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(1) due to constant-time operations.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`easy` `math`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n%2 == 0:
            return n
        return n*2 
```

</details>
