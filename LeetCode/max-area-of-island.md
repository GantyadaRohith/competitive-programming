# 🟠 max-area-of-island — Max Area of Island

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/max-area-of-island/) &nbsp;|&nbsp; **Solved:** 2025-12-18

---

## 📝 Summary

Given a 2D binary grid, find the largest area of an island where an island is defined as a group of 1's connected horizontally or vertically.

## 🔍 Key Observation

The key insight is to use Depth-First Search (DFS) to explore each island and calculate its area.

## ⚙️ Algorithm

1. Initialize a visited matrix to keep track of visited cells and the grid dimensions.
2. Define a DFS function to explore an island starting from a given cell.
3. For each cell, if it's part of an island (1) and not visited, perform DFS to calculate the area of the island.
4. Update the maximum area found during the DFS traversal.
5. Iterate through the grid, starting DFS from each unvisited cell that is part of an island.
6. Return the maximum area found.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n * m) where n is the number of rows and m is the number of columns in the grid.` | `O(n * m) for the visited matrix and the recursion stack in the worst case.` |

## 🏷️ Tags

`dfs` `grid` `island` `area`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row,cols = len(grid),len(grid[0])
        visited = [[False]*cols for _ in range(row)]
        d = [(1,0),(-1,0),(0,1),(0,-1)]
        def dfs(r,c):
            if r<0 or r>= row or c<0 or c>= cols:
                return 0
            if visited[r][c] or grid[r][c] == 0:
                return 0
            visited[r][c] = True
            area = 1

            for dr,dc in d:
                area+=dfs(r+dr,c+dc)
            return area

        max_area = 0
        for i in range(row):
            for j in range(cols):
                if grid[i][j] == 1 and not visited[i][j]:
                    max_area = max(max_area,dfs(i,j))
        return max_area
```

</details>
