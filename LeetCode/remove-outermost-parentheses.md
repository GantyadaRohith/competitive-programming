# 🟠 remove-outermost-parentheses — Remove Outermost Parentheses

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/remove-outermost-parentheses/) &nbsp;|&nbsp; **Solved:** 2026-07-13

---

## 📝 Summary

Given a string of parentheses, remove the outermost parentheses of each group of valid parentheses.

## 🔍 Key Observation

The solution uses a counter to track the balance of parentheses and appends characters to the result string only when the balance is greater than zero, ensuring the outermost parentheses are removed.

## ⚙️ Algorithm

1. Initialize an empty string `res` and a counter `op` to zero.
2. Iterate through each character in the input string `s`:
   - If the character is '(', increment `op` and append it to `res` if `op` is greater than zero.
   - If the character is ')', decrement `op` and append it to `res` if `op` is greater than zero.
3. Return the resulting string `res`.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) where n is the length of the input string `s`, as each character is processed once.` | `O(1) auxiliary space, as only a few extra variables are used.` |

## 🏷️ Tags

`short` `python` `stack` `parentheses`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = ''
        op = 0
        for i in range(len(s)):
            if s[i] == '(':
                if op > 0:
                    res = res + s[i]
                op+=1
            elif s[i] == ')':
                op-=1
                if op>0:
                    res = res + s[i]
        return res
```

</details>
