# 🟠 reverse-bits — Reverse Bits

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/reverse-bits/) &nbsp;|&nbsp; **Solved:** 2025-12-09

---

## 📝 Summary

Reverse the bits of an integer.

## 🔍 Key Observation

The key insight is to convert the integer to a binary string, reverse it, and then convert it back to an integer.

## ⚙️ Algorithm

1. Convert the integer `n` to a binary string of length 32 using `format(n, '032b')`. This ensures that the binary string is zero-padded to 32 bits.
2. Reverse the binary string using slicing (`x[::-1]`).
3. Convert the reversed binary string back to an integer using `int(x, 2)`.
4. Return the resulting integer.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(1) due to the fixed length of the binary string.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`short` `lowercase` `bit manipulation` `reverse`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def reverseBits(self, n: int) -> int:
        x = str(format(n,'032b'))
        x = x[::-1]
        x = int(x,2)
        return x

```

</details>
