# 🟠 longest-common-subsequence — Longest Common Subsequence

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/longest-common-subsequence/) &nbsp;|&nbsp; **Solved:** 2026-07-11

---

## 📝 Summary

Given two strings, find the length of the longest common subsequence.

## 🔍 Key Observation

Dynamic programming is used to build a table where each cell contains the length of the longest common subsequence of the substrings up to that point.

## ⚙️ Algorithm

1. Initialize a 2D array `dp` of size `(m+1) x (n+1)` where `m` and `n` are the lengths of `text1` and `text2` respectively. Set `dp[0][0]` to 0.
2. Iterate through each character of `text1` and `text2` using nested loops.
3. If the characters match, set `dp[i][j] = dp[i-1][j-1] + 1`.
4. If the characters do not match, set `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`.
5. The value at `dp[m][n]` will be the length of the longest common subsequence.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(m * n)` | `O(m * n)` |

## 🏷️ Tags

`dp` `longest` `common` `subsequence`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n = len(text1),len(text2)
        dp = [([0]*(n+1)) for _ in range(m+1)]
        dp[0][0] = 0
        for i in range(1,m+1):
            for j in range(1,n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        return dp[-1][-1]

```

</details>
