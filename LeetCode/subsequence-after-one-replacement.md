# 🟠 subsequence-after-one-replacement — Subsequence After One Replacement

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/subsequence-after-one-replacement/) &nbsp;|&nbsp; **Solved:** 2026-07-18

---

## 📝 Summary

Determine if a subsequence of t can be formed by replacing at most one character in s.

## 🔍 Key Observation

Use two pointers to track the current positions in s and t, allowing for one replacement.

## ⚙️ Algorithm

Iterate through t, using two pointers i and j. If s[i] matches t[j], move i forward. If s[j] matches t[j], move j forward. If s[i] does not match t[j], increment i and check if s[j] matches t[j]. If i or j reaches the end of s, return True if a valid subsequence is found.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) where n is the length of t, as each character in t is processed at most twice.` | `O(1) auxiliary space, as only a few extra variables are used.` |

## 🏷️ Tags

`string` `two pointers` `subsequence`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def canMakeSubsequence(self, s: str, t: str) -> bool:
        m,n = len(s),len(t)
        if m > n:
            return False
        i,j = 0,0
        for ch in t:
            if s[i] == ch:
                i+=1
            i = max(i,j+1)
            if s[j] == ch:
                j+=1
            if i==m or j == m:
                return True
        return False


```

</details>
