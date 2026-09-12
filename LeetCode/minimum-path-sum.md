# 🟠 minimum-path-sum — Minimum Path Sum

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/minimum-path-sum/) &nbsp;|&nbsp; **Solved:** 2026-07-11

---

## 📝 Summary

Given a grid of non-negative integers, find the minimum path sum from the top-left corner to the bottom-right corner, moving only right or down.

## 🔍 Key Observation

The problem can be solved using dynamic programming to build up a solution from smaller subproblems.

## ⚙️ Algorithm

1. Initialize a 2D array `dp` of the same size as the grid to store the minimum path sums to each cell. Set the top-left cell to the value of the grid's top-left cell.
2. Fill the first row of `dp` by summing the values of the grid's first row and the corresponding `dp` values from the previous row.
3. Fill the first column of `dp` by summing the values of the grid's first column and the corresponding `dp` values from the previous column.
4. For each cell (i, j) in the grid (except the first row and column), set `dp[i][j]` to the minimum of the values from the cell directly above (`dp[i-1][j]`) and the cell directly to the left (`dp[i][j-1]`), plus the value of the grid cell at (i, j).
5. The value at `dp[-1][-1]` will be the minimum path sum from the top-left to the bottom-right corner.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(m * n) due to the nested loops that fill the `dp` array.` | `O(m * n) auxiliary space used for the `dp` array.` |

## 🏷️ Tags

`dp` `grid` `path` `sum`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [([0]*len(grid[0])) for _ in range(len(grid))]
        m,n = len(grid),len(grid[0])
        dp[0][0] = grid[0][0]
        for i in range(1,n):
            dp[0][i] = dp[0][i-1] + grid[0][i]
        for i in range(1,m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + grid[i][j]
        return dp[-1][-1]
```

</details>
