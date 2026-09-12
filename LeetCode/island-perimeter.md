# 🟠 island-perimeter — Island Perimeter

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/island-perimeter/) &nbsp;|&nbsp; **Solved:** 2026-08-02

---

## 📝 Summary

Calculate the perimeter of an island in a grid where 1 represents land and 0 represents water.

## 🔍 Key Observation

The perimeter is determined by counting the number of land cells that are on the edge of the grid or adjacent to water cells.

## ⚙️ Algorithm

The solution uses Depth-First Search (DFS) to traverse the grid. For each land cell, it checks its four adjacent cells. If an adjacent cell is water or out of bounds, it increments the perimeter count. The DFS ensures that each land cell is only visited once.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n * m) where n is the number of rows and m is the number of columns in the grid.` | `O(n * m) due to the visited array and the recursive call stack.` |

## 🏷️ Tags

`dfs` `grid` `perimeter`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row,cols = len(grid),len(grid[0])
        d = [(1,0),(-1,0),(0,1),(0,-1)]
        cnt = 0
        visited = [[False for _ in range(cols)] for _ in range(row)]
        def dfs(r,c):
            nonlocal cnt
            if r<0 or r>=row or c<0 or c>=cols:
                cnt+=1
                return
            if grid[r][c] != 1:
                cnt+=1
                return
            if visited[r][c]:
                return 
            visited[r][c] = True
            for dr,dc in d:
                dfs(r+dr,c+dc)
        for i in range(row):
            for j in range(cols):
                if grid[i][j] == 1:
                    dfs(i,j)
                    break
        return cnt
                
        
```

</details>
