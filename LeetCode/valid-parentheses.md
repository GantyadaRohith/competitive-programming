# 🟠 valid-parentheses — Valid Parentheses

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/valid-parentheses/) &nbsp;|&nbsp; **Solved:** 2026-07-08

---

## 📝 Summary

Determine if a string of parentheses is valid by matching opening and closing brackets.

## 🔍 Key Observation

Use a stack to keep track of opening brackets and match them with closing brackets.

## ⚙️ Algorithm

Iterate through each character in the string. If it's an opening bracket, push it onto the stack. If it's a closing bracket, check if the stack is empty or if the top of the stack doesn't match the corresponding opening bracket. If the stack is empty at the end, the string is valid.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) where n is the length of the string, as each character is processed once.` | `O(n) in the worst case, where all characters are opening brackets.` |

## 🏷️ Tags

`stack` `parentheses` `validation`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s: 
            if i in {'(','[','{'}:
                stack.append(i)
            elif not stack and i in '})]':
                return False
            elif i == ')'  and stack[-1] == '(':
                stack.pop()
            elif i == '}' and stack[-1] == '{':
                stack.pop()
            elif i == ']'  and stack[-1] == '[':
                stack.pop()
            else:
                return False
        return len(stack) == 0
```

</details>
