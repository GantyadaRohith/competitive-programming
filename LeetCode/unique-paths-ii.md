# 🟠 unique-paths-ii — Unique Paths II

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/unique-paths-ii/) &nbsp;|&nbsp; **Solved:** 2026-03-07

---

## 📝 Summary

Given a 2D grid with obstacles, find the number of unique paths from the top-left corner to the bottom-right corner.

## 🔍 Key Observation

Use dynamic programming to build up the solution iteratively.

## ⚙️ Algorithm

1. Initialize a 2D DP array where `dp[i][j]` represents the number of unique paths to reach cell `(i, j)`. 2. Set `dp[0][0]` to 1 if the starting cell is not an obstacle. 3. Fill the first row and first column of the DP array based on whether the cells are obstacles. 4. For each cell `(i, j)`, if it is not an obstacle, update `dp[i][j]` as the sum of the paths from the cell above (`dp[i-1][j]`) and the cell to the left (`dp[i][j-1]`). 5. The value at `dp[m-1][n-1]` will be the number of unique paths to the bottom-right corner.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(m * n) due to the nested loops iterating over the grid.` | `O(m * n) for the DP array.` |

## 🏷️ Tags

`dp` `grid` `path` `unique`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        dp = [[0]*n for _ in range(m)]
        
        if grid[0][0] == 1:
            return 0
        
        dp[0][0] = 1
        
        for i in range(1,m):
            if grid[i][0] == 0:
                dp[i][0] = dp[i-1][0]
        
        for j in range(1,n):
            if grid[0][j] == 0:
                dp[0][j] = dp[0][j-1]
        
        for i in range(1,m):
            for j in range(1,n):
                if grid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]
```

</details>
