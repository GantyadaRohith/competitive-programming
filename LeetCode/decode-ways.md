# 🟠 decode-ways — Decode Ways

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/decode-ways/) &nbsp;|&nbsp; **Solved:** 2026-07-12

---

## 📝 Summary

Given a string of digits, decode it into the number of ways to decode it as a sequence of letters.

## 🔍 Key Observation

The problem involves decoding a string where each digit can represent a letter (1-26) and two digits can represent a letter (10-26).

## ⚙️ Algorithm

The solution uses dynamic programming to count the number of ways to decode the string. It initializes a DP array where `dp[i]` represents the number of ways to decode the substring `s[0:i]`. It iterates through the string, updating the DP array based on whether the current digit or the two preceding digits can form a valid letter.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to a single pass through the string.` | `O(n) auxiliary space for the DP array.` |

## 🏷️ Tags

`dp` `string` `coding`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def numDecodings(self, s: str) -> int:
        s = s.strip()
        n = len(s)
        if n == 0 or s[0] == '0':
            return 0
        dp = [0] *(n+1)
        dp[0] = dp[1] = 1
        for i in range(2,n+1):
                if s[i-1] != '0':
                    dp[i] = dp[i-1]
                two = int(s[i-2:i])
                if 10<=two<=26:
                    dp[i]+=dp[i-2]
        return dp[n]
                
```

</details>
