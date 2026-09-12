# 🟠 count-commas-in-range — Count Commas in Range

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/count-commas-in-range/) &nbsp;|&nbsp; **Solved:** 2026-09-09

---

## 📝 Summary

Count the number of commas in a range of numbers.

## 🔍 Key Observation

The problem can be solved by directly subtracting 999 from the input number if it is greater than 999.

## ⚙️ Algorithm

The solution involves checking if the input number `n` is greater than 999. If it is, the function returns `n-999`, which represents the number of commas in the range. If `n` is 999 or less, the function returns 0, as there are no commas in the range.

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
    def countCommas(self, n: int) -> int:
        if n < 999:
            return 0
        else:
            return n-999
```

</details>
