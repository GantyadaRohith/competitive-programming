# 🟠 check-ascii-palindromic — Check ASCII Palindromic

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/check-ascii-palindromic/) &nbsp;|&nbsp; **Solved:** 2026-08-23

---

## 📝 Summary

Determine if a given string is an ASCII palindromic string.

## 🔍 Key Observation

Convert each character to its binary representation and check if the resulting binary string is a palindrome.

## ⚙️ Algorithm

1. Convert each character in the string to its 8-bit binary representation using `ord(i):08b`.
2. Join all binary strings into a single string.
3. Check if the joined string is equal to its reverse.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n), where n is the length of the string, due to the conversion and concatenation operations.` | `O(n), as we store the binary representations of the characters.` |

## 🏷️ Tags

`ascii` `palindrome` `binary`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def isPalindromic(self, s: str) -> bool:
        out = []
        for i in s:
            out.append(f"{ord(i):08b}")
        s = ''.join(out)
        print(s)
        return True if s == s[::-1] else False
```

</details>
