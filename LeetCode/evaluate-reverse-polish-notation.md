# 🟠 evaluate-reverse-polish-notation — Evaluate Reverse Polish Notation

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/evaluate-reverse-polish-notation/) &nbsp;|&nbsp; **Solved:** 2025-12-13

---

## 📝 Summary

Evaluate Reverse Polish Notation (RPN) expression.

## 🔍 Key Observation

Use a stack to process the tokens and apply operations in the correct order.

## ⚙️ Algorithm

Iterate through each token in the input list. If it's an operand, convert it to an integer and push it onto the stack. If it's an operator, pop the top two elements from the stack, apply the operation, and push the result back onto the stack. Continue this process until all tokens are processed.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n), where n is the number of tokens in the input list.` | `O(n), due to the stack used to store operands.` |

## 🏷️ Tags

`stack` `rpn` `evaluation`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = []
        for i in tokens:
            if i not in {'+','*','-','/'}:
                res.append(int(i))
            else:
                b = res.pop()
                a = res.pop()
                if i == '+':
                    res.append(a+b)
                elif i == '-':
                    res.append(a-b)
                elif i == '*':
                    res.append(a*b)
                elif i == '/':
                    res.append(int(a/b))
        return res.pop()
```

</details>
