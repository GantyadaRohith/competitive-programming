# 🟠 basic-calculator — Basic Calculator

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/basic-calculator/) &nbsp;|&nbsp; **Solved:** 2026-07-11

---

## 📝 Summary

Implement a basic calculator to evaluate arithmetic expressions.

## 🔍 Key Observation

The use of a stack to handle operator precedence and parentheses.

## ⚙️ Algorithm

The solution uses a recursive function `calc` to parse the expression. It iterates through the string, handling digits, operators, and parentheses. The stack is used to manage the operands and operators, ensuring correct order of operations is applied.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to a single pass through the string.` | `O(n) for the stack and other variables.` |

## 🏷️ Tags

`stack` `lowercase` `calculator` `tags`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def calculate(self, s):    
        def calc(it):
            def update(op, v):
                if op == "+": stack.append(v)
                if op == "-": stack.append(-v)
        
            num, stack, sign = 0, [], "+"
            
            while it < len(s):
                if s[it].isdigit():
                    num = num * 10 + int(s[it])
                elif s[it] in "+-*/":
                    update(sign, num)
                    num, sign = 0, s[it]
                elif s[it] == "(":
                    num, j = calc(it + 1)
                    it = j - 1
                elif s[it] == ")":
                    update(sign, num)
                    return sum(stack), it + 1
                it += 1
            update(sign, num)
            return sum(stack)

        return calc(0)
```

</details>
