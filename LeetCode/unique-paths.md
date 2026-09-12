# 🟠 unique-paths — Unique Paths

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/unique-paths/) &nbsp;|&nbsp; **Solved:** 2026-07-09

---

## 📝 Summary

Given a grid of size m x n, calculate the number of unique paths from the top-left corner to the bottom-right corner, moving only right or down.

## 🔍 Key Observation

The problem can be solved using dynamic programming, where each cell in the grid represents the number of unique paths to reach that cell.

## ⚙️ Algorithm

1. Initialize a 2D list `dp` of size m x n with all elements set to -1. This list will store the number of unique paths to each cell.
2. Set the first row and first column of `dp` to 1 because there is exactly one way to reach any cell in the first row or column (by moving only right or down, respectively).
3. Iterate through the grid starting from the second row and second column. For each cell, calculate the number of unique paths by summing the values from the cell directly above and the cell directly to the left.
4. The value in the bottom-right corner of `dp` will be the total number of unique paths from the top-left corner to the bottom-right corner.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(m * n) due to the nested loops iterating through the grid.` | `O(m * n) auxiliary space used for the `dp` list.` |

## 🏷️ Tags

`dp` `grid` `paths`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1]*n for _ in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for i in range(n):
            dp[0][i] = 1
        for i in range(1,m):
            for j in range(1,n):
                if dp[i][j] == -1:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
```

</details>
