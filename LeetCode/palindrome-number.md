# 🟠 palindrome-number — Palindrome Number

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/palindrome-number/) &nbsp;|&nbsp; **Solved:** 2025-12-10

---

## 📝 Summary

Determine if a given integer is a palindrome.

## 🔍 Key Observation

Convert the integer to a string and reverse it to compare with the original.

## ⚙️ Algorithm

1. Convert the integer to a string.
2. Reverse the string.
3. Compare the reversed string with the original string.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to string conversion and reversal.` | `O(n) for storing the reversed string.` |

## 🏷️ Tags

`easy` `string` `palindrome`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        rev=x[::-1]  
        return rev==x  
        
```

</details>
