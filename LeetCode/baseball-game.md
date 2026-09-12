# 🟠 baseball-game — Baseball Game

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/baseball-game/) &nbsp;|&nbsp; **Solved:** 2026-07-08

---

## 📝 Summary

Given a list of strings representing operations in a baseball game, calculate the final score.

## 🔍 Key Observation

The use of a stack to keep track of scores allows for efficient calculation of scores based on operations like 'C' (clear last score), 'D' (double last score), and '+' (add the last two scores).

## ⚙️ Algorithm

1. Initialize an empty stack to keep track of scores.
2. Iterate through each operation in the list:
   - If the operation is a number, convert it to an integer and push it onto the stack.
   - If the operation is 'C', pop the last score from the stack.
   - If the operation is 'D', double the last score and push it onto the stack.
   - If the operation is '+', add the last two scores and push the result onto the stack.
3. Sum the scores in the stack to get the final score.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to a single pass through the operations list.` | `O(n) for the stack to store scores.` |

## 🏷️ Tags

`stack` `simulation` `baseball`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        def is_integer(s):
            try:
                int(s)
                return True
            except ValueError:
                return False
        for i in operations:
            if is_integer(i):
                stack.append(int(i))
            elif i == 'C':
                stack.pop()
            elif i == 'D':
                stack.append(stack[-1]*2)
            elif i == '+':
                stack.append(stack[-1]+stack[-2])
        return sum(stack)
```

</details>
