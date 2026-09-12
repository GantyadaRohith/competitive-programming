# 🟠 valid-palindrome — Valid Palindrome

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/valid-palindrome/) &nbsp;|&nbsp; **Solved:** 2026-05-17

---

## 📝 Summary

Determine if a given string is a palindrome, ignoring non-alphanumeric characters and case.

## 🔍 Key Observation

Normalize the string by converting it to lowercase and removing non-alphanumeric characters before comparing.

## ⚙️ Algorithm

1. Initialize two pointers, `i` at the start and `j` at the end of the string.
2. While `i` is less than `j`:
   - Move `i` forward until it points to a alphanumeric character.
   - Move `j` backward until it points to a alphanumeric character.
   - Compare the characters at `i` and `j` (after normalization), and if they are not equal, return `False`.
   - Increment `i` and decrement `j`.
3. If the loop completes without finding any mismatch, return `True`.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to the single pass through the string.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`string` `palindrome` `algorithm`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s)<=1:
            return True
        i = 0
        j = len(s)-1
        while i < j:

            while i < j and not s[i].isalnum():
                i += 1
        
            while i < j and not s[j].isalnum():
                j -= 1
        
            if s[i].lower() != s[j].lower():
                return False
        
            i += 1
            j -= 1
        return True

```

</details>
