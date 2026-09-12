# 🟠 remove-k-digits — Remove K Digits

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/remove-k-digits/) &nbsp;|&nbsp; **Solved:** 2025-11-27

---

## 📝 Summary

Given a non-negative integer represented as a string and an integer k, remove k digits from the number to make it as small as possible.

## 🔍 Key Observation

The key insight is to use a stack to maintain a non-decreasing sequence of digits, which helps in removing unnecessary digits.

## ⚙️ Algorithm

1. Initialize an empty stack and iterate through each digit in the input number.
2. For each digit, while the stack is not empty, k is greater than 0, and the top of the stack is greater than the current digit, pop the stack and decrement k.
3. Push the current digit onto the stack.
4. After processing all digits, while k is greater than 0, pop elements from the stack to remove the remaining k digits.
5. Join the stack elements into a string and remove leading zeros.
6. Return the result or '0' if the result is empty.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n), where n is the length of the input string.` | `O(n), where n is the length of the input string.` |

## 🏷️ Tags

`stack` `string` `remove` `digits`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack =[]
        for digit in num:
        	while stack and k>0 and stack[-1] > digit:
        		stack.pop()
        		k-=1
        	stack.append(digit)
        while k>0:
        	stack.pop()
        	k-=1
        result = "".join(stack).lstrip('0')
        return result if result!= "" else '0'
```

</details>
