# 🟠 longest-palindromic-substring — Longest Palindromic Substring

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/longest-palindromic-substring/) &nbsp;|&nbsp; **Solved:** 2026-07-08

---

## 📝 Summary

Find the longest palindromic substring in a given string.

## 🔍 Key Observation

Expand around the center to find palindromes of odd and even lengths.

## ⚙️ Algorithm

Iterate through each character in the string, treating it as the center of a potential palindrome. Expand outwards while the characters on both sides are equal. Keep track of the longest palindrome found.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n^2) due to the nested loops expanding around each character.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`string` `palindrome` `expand around center`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s==s[::-1]:
            return s
        start, max_len = 0, 1
        def expand(left, right):
            nonlocal start, max_len
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > max_len:
                    max_len = right - left + 1
                    start = left
                left -= 1
                right += 1
        for i in range(len(s)):
            expand(i, i)
            expand(i, i + 1)
        return s[start:start + max_len]
```

</details>
