# 🟠 number-of-islands — Number of Islands

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/number-of-islands/) &nbsp;|&nbsp; **Solved:** 2025-12-18

---

## 📝 Summary

Count the number of distinct islands in a grid where '1' represents land and '0' represents water.

## 🔍 Key Observation

Use Depth-First Search (DFS) to explore each island and mark visited cells.

## ⚙️ Algorithm

1. Initialize a visited matrix to keep track of visited cells.
2. Define a DFS function to explore an island starting from a given cell.
3. For each '1' cell, if it hasn't been visited, increment the island count and perform DFS to mark all connected land cells as visited.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n * m) where n is the number of rows and m is the number of columns in the grid.` | `O(n * m) for the visited matrix and the recursive call stack in the worst case.` |

## 🏷️ Tags

`dfs` `grid` `count`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row,cols = len(grid),len(grid[0])
        dir = [(1,0),(-1,0),(0,1),(0,-1)]
        visited = [[False]*cols for _ in range(row)]
        cnt = 0
        def dfs(l,r):
            if l<0 or l>=len(grid) or r<0 or r>=len(grid[0]) :
                return 
            if visited[l][r] or grid[l][r] == '0':
                return
            visited[l][r] = True
            for dr,dc in dir:
                dfs(l+dr,r+dc)

        island = 0
        for r in range(row):
            for c in range(cols):
                if grid[r][c] == '1' and not visited[r][c]:
                    dfs(r,c)
                    cnt+=1
        return cnt
```

</details>
