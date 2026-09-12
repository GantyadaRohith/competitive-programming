# 🟠 smallest-palindromic-rearrangement-i — Smallest Palindromic Rearrangement I

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/smallest-palindromic-rearrangement-i/) &nbsp;|&nbsp; **Solved:** 2026-07-28

---

## 📝 Summary

Given a string, rearrange it to form the smallest palindromic string by rearranging its characters.

## 🔍 Key Observation

The solution involves sorting the first half of the string and then appending the sorted first half to the reversed second half, ensuring the string is palindromic.

## ⚙️ Algorithm

1. Check if the string length is 1, in which case it is already a palindrome. 2. Sort the first half of the string. 3. If the string length is odd, append the middle character to the end of the sorted first half. 4. If the string length is even, concatenate the sorted first half with its reverse.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log n) due to sorting.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`sort` `palindrome` `rearrangement`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def smallestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        mid = (len(s)//2)-1
        a = sorted(s[:mid+1])
        res = ''
        if len(s)&1:
            rev = a[::-1]
            res = ''.join(a) + s[mid+1] + ''.join(a[::-1])
        else:
            res = ''.join(a+a[::-1])
        return res
```

</details>
