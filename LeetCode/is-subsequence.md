# 🟠 is-subsequence — Is Subsequence

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/is-subsequence/) &nbsp;|&nbsp; **Solved:** 2026-07-12

---

## 📝 Summary

Determine if one string is a subsequence of another.

## 🔍 Key Observation

Use two pointers to traverse both strings efficiently.

## ⚙️ Algorithm

Initialize two pointers, i for s and j for t. Move i forward when a match is found. Return True if i reaches the end of s.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) where n is the length of s.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`string` `two pointers` `subsequence`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i,j = 0,0
        while i<len(s) and j<len(t):
            if s[i] == t[j]:
                i+=1
            j+=1
        print(i)
        print(len(s))
        if i == len(s):
            return True
        return False
```

</details>
