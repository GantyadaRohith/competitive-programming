# 🟠 count-commas-in-range — Count Commas in Range

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/count-commas-in-range/) &nbsp;|&nbsp; **Solved:** 2026-09-09

---

## 📝 Summary

Calculates the total count of 'thousands separator' commas for integers from 1 to `n`, where each integer 1000 or greater contributes exactly one comma.

## 🔍 Key Observation

Integers from 1 to 999 have no commas. Each integer from 1000 to `n` contributes a single comma to the total count.

## ⚙️ Algorithm

**Direct calculation**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(1)` | `O(1)` |

## 🏷️ Tags

`math` `counting` `ad-hoc` `arithmetic`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def countCommas(self, n: int) -> int:
        if n < 999:
            return 0
        else:
            return n-999
```

</details>
