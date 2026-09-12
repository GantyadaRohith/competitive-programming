# 🟠 number-of-common-factors — Number of Common Factors

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/number-of-common-factors/) &nbsp;|&nbsp; **Solved:** 2026-07-25

---

## 📝 Summary

Given two integers, find the number of common factors between them.

## 🔍 Key Observation

The key insight is to iterate through all numbers from 1 to 1000 and check if they are factors of both input numbers.

## ⚙️ Algorithm

1. Initialize an empty set `s` to store common factors.
2. Iterate through numbers from 1 to 1000.
3. For each number `i`, check if it divides both `a` and `b` without a remainder.
4. If it does, add `i` to the set `s`.
5. Return the size of the set `s`, which represents the number of common factors.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(1000) = O(1) due to the fixed range of numbers.` | `O(n) where n is the number of common factors, but in practice, it's O(1000) due to the fixed range.` |

## 🏷️ Tags

`easy` `math` `set`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        s = set()
        for i in range(1,1001):
            if a%i == 0 and b%i == 0:
                s.add(i)
        return len(s)
```

</details>
