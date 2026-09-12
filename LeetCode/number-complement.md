# 🟠 number-complement — Number Complement

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/number-complement/) &nbsp;|&nbsp; **Solved:** 2026-07-25

---

## 📝 Summary

Given a non-negative integer, find its bitwise complement.

## 🔍 Key Observation

The bitwise complement of a number is obtained by flipping all its bits.

## ⚙️ Algorithm

1. Initialize an empty string `s` to store the complement bits.
2. Use a while loop to iterate through each bit of the number:
   - If the current bit is 1, append '0' to `s`.
   - If the current bit is 0, append '1' to `s`.
   - Right shift the number by 1 bit.
3. Reverse the string `s` to get the final complement.
4. Convert the reversed string to an integer and return it.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to the loop iterating through each bit of the number.` | `O(n) for storing the complement bits.` |

## 🏷️ Tags

`bitwise` `complement` `number`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def findComplement(self, num: int) -> int:
        if num == 0:
            return 1

        s = ""

        while num:
            if num & 1:
                s += "0"
            else:
                s += "1"
            num >>= 1

        s = s[::-1]
        return int(s, 2)
```

</details>
