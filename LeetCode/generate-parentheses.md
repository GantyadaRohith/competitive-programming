# 🟠 generate-parentheses — Generate Parentheses

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/generate-parentheses/) &nbsp;|&nbsp; **Solved:** 2026-07-12

---

## 📝 Summary

Generate all valid combinations of n pairs of parentheses.

## 🔍 Key Observation

Use dynamic programming to build valid combinations by considering the number of open and close parentheses.

## ⚙️ Algorithm

The solution uses a recursive function `dp(op, cp)` to generate valid combinations. It checks if the current state `(op, cp)` has already been computed and stores the result in a memoization table. If not, it recursively generates combinations by adding an open or close parenthesis and updates the memoization table with the results.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(4^n / sqrt(n)) due to the Catalan number growth and memoization.` | `O(n^2) for the memoization table.` |

## 🏷️ Tags

`dynamic-programming` `parentheses` `combinations`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        table = {}
        def dp(op, cp):
            # check memo
            if (op, cp) in table:
                return table[(op, cp)]

            if op == n and cp == n:
                return [""]

            res = []

            if op < n:
                for s in dp(op + 1, cp):
                    res.append("(" + s)

            if cp < op:
                for s in dp(op, cp + 1):
                    res.append(")" + s)

            table[(op, cp)] = res
            return res

        return dp(0,0)
```

</details>
