# 🟠 complement-of-base-10-integer — Complement of Base 10 Integer

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/complement-of-base-10-integer/) &nbsp;|&nbsp; **Solved:** 2026-07-25

---

## 📝 Summary

Given a non-negative integer n, return its complement number. The complement of a number is the number you get when you flip all the bits in its binary representation.

## 🔍 Key Observation

The key insight is to use bitwise operations to flip each bit of the number.

## ⚙️ Algorithm

1. Initialize an empty string `s` to store the binary representation of the complement.
2. Use a while loop to iterate through each bit of the number `n`:
   - If the current bit is 1, append '0' to `s`.
   - If the current bit is 0, append '1' to `s`.
   - Right shift `n` by 1 bit to process the next bit.
3. Reverse the string `s` to get the binary representation of the complement.
4. Convert the reversed string `s` to an integer and return it.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(log n) due to the right shift operation.` | `O(log n) auxiliary space for storing the binary representation.` |

## 🏷️ Tags

`bitwise` `complement` `binary`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1

        s = ""

        while n:
            if n & 1:
                s += "0"
            else:
                s += "1"
            n >>= 1

        s = s[::-1]
        return int(s, 2)
```

</details>
