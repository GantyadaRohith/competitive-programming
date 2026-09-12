# 🟠 edit-distance — Edit Distance

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/edit-distance/) &nbsp;|&nbsp; **Solved:** 2026-07-09

---

## 📝 Summary

Given two strings, find the minimum number of single-character edits (insertions, deletions, or substitutions) required to convert one string into the other.

## 🔍 Key Observation

The problem can be solved using dynamic programming with a 2D table to store the minimum edit distances between substrings of the two words.

## ⚙️ Algorithm

1. Initialize a 2D table `dp` where `dp[i][j]` represents the minimum edit distance between the first `i` characters of `word1` and the first `j` characters of `word2`. Initialize the first row and column to represent the cost of converting an empty string to a string of length `j` or `i` respectively.
2. For each character in `word1` and `word2`, compare them:
   - If they are the same, the cost remains the same as the previous diagonal cell (`dp[i-1][j-1]`).
   - If they are different, the cost is 1 plus the minimum of the three possible operations: insertion (`dp[i-1][j]`), deletion (`dp[i][j-1]`), or substitution (`dp[i-1][j-1]`).
3. The value at `dp[m][n]` will be the minimum edit distance between the entire two words.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(m * n), where m and n are the lengths of the two words.` | `O(m * n) for the 2D table.` |

## 🏷️ Tags

`short` `lowercase` `dp` `edit-distance`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n = len(word1),len(word2)
        dp = [[0]*(len(word2)+1) for _ in range(len(word1)+1)]
        for i in range(m+1):
            dp[i][0] = i
        for j in range(n+1):
            dp[0][j] = j
        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1+min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])
        return dp[-1][-1]
```

</details>
