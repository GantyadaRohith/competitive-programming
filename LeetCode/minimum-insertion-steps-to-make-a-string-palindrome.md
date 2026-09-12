# 🟠 minimum-insertion-steps-to-make-a-string-palindrome — Minimum Insertion Steps to Make a String Palindrome

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/) &nbsp;|&nbsp; **Solved:** 2025-12-10

---

## 📝 Summary

Given a string, find the minimum number of characters to insert to make it a palindrome.

## 🔍 Key Observation

The problem can be solved using dynamic programming to find the longest palindromic subsequence.

## ⚙️ Algorithm

The solution uses a recursive function `f(i, j)` that calculates the minimum number of insertions needed to make the substring `s[i:j+1]` a palindrome. It uses memoization to store previously computed results to avoid redundant calculations. The base case is when `i >= j`, in which case no insertions are needed. If the characters at positions `i` and `j` are the same, the function returns the result of `f(i+1, j-1)`. Otherwise, it returns 1 plus the minimum of `f(i+1, j)` and `f(i, j-1)`, representing the choice to insert a character at either end of the substring.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n^2) due to the nested loops and memoization.` | `O(n^2) for the memoization table.` |

## 🏷️ Tags

`dynamic programming` `longest palindromic subsequence` `memoization`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [[-1] * n for _ in range(n)]

        def f(i, j):
            
            if i >= j:
                return 0

            
            if dp[i][j] != -1:
                return dp[i][j]

            
            if s[i] == s[j]:
                dp[i][j] = f(i + 1, j - 1)
            else:
                
                dp[i][j] = 1 + min(
                    f(i + 1, j),   
                    f(i, j - 1)   
                )

            return dp[i][j]

        return f(0, len(s) - 1)
```

</details>
