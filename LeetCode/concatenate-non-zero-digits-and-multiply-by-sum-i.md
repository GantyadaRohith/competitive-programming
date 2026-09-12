# 🟠 concatenate-non-zero-digits-and-multiply-by-sum-i — Concatenate Non-Zero Digits and Multiply by Sum I

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-i/) &nbsp;|&nbsp; **Solved:** 2026-07-08

---

## 📝 Summary

Given a non-negative integer, concatenate its non-zero digits and multiply the result by the sum of its digits.

## 🔍 Key Observation

The key insight is to iterate through the digits, build a new string with non-zero digits, and calculate the sum of these digits.

## ⚙️ Algorithm

1. Initialize an empty string `s` to store non-zero digits and a variable `su` to store the sum of these digits.
2. Convert the integer `n` to a string and iterate through each character.
3. If the character is not '0', append it to `s` and add its numeric value to `su`.
4. After processing all characters, convert `s` back to an integer and multiply it by `su`.
5. Return the result. If `s` is empty, return 0.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) where n is the number of digits in the input number.` | `O(n) for storing the non-zero digits in the string `s`.` |

## 🏷️ Tags

`string` `math` `digits`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def sumAndMultiply(self, n: int) -> int:
        su = 0
        s = ''
        for i in str(n):
            if i != '0':
                s += i
                su += ord(i) - ord('0')
        return int(s)*su if len(s) != 0 else 0
```

</details>
