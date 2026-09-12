# 🟠 check-ascii-palindromic — Check ASCII Palindromic

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/check-ascii-palindromic/) &nbsp;|&nbsp; **Solved:** 2026-08-23

---

## 📝 Summary

The problem asks to determine if an input string is palindromic when each character is replaced by its 8-bit ASCII binary representation.

## 🔍 Key Observation

The palindromic check must be performed on the concatenated 8-bit binary representations of the original string's characters, not on the original string itself.

## ⚙️ Algorithm

**Character-wise ASCII to binary conversion followed by a standard string palindrome check.**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(N)` | `O(N)` |

## 🏷️ Tags

`string` `binary` `palindrome` `ascii`

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
