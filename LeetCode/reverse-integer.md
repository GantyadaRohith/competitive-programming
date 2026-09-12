# 🟠 reverse-integer — Reverse Integer

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/reverse-integer/) &nbsp;|&nbsp; **Solved:** 2025-11-21

---

## 📝 Summary

Reverses a given integer while handling overflow cases.

## 🔍 Key Observation

The solution uses a loop to reverse the digits of the integer and checks for overflow before returning the result.

## ⚙️ Algorithm

1. Check if the input integer is within the range of a 32-bit signed integer. If not, return 0.
2. Determine the sign of the input integer.
3. Convert the input integer to its absolute value.
4. Use a loop to reverse the digits of the integer by repeatedly taking the last digit, adding it to the reversed number, and removing the last digit from the original number.
5. Check if the reversed number is within the range of a 32-bit signed integer. If not, return 0.
6. Return the reversed number with the original sign.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to the loop that processes each digit of the integer.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`python` `integer` `reverse`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def reverse(self, x: int) -> int:
        if x > 2**31 - 1 or x < 2**31 * -1:
            return 0 
        sign = -1 if x < 0 else 1
        x = abs(x)  
        rev = 0
        while x > 0 :
            rev = rev*10 + x%10
            x//=10
        if rev > 2**31 - 1 or rev < 2**31 * -1:
            return 0 
        return rev*sign
```

</details>
