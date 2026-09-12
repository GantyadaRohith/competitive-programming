# 🟠 path-with-maximum-gold — Path with Maximum Gold

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/path-with-maximum-gold/) &nbsp;|&nbsp; **Solved:** 2026-07-11

---

## 📝 Summary

Find the path with the maximum gold in a grid where each cell contains a certain amount of gold.

## 🔍 Key Observation

The key insight is to use depth-first search (DFS) to explore all possible paths and keep track of the maximum gold collected.

## ⚙️ Algorithm

1. Define a DFS function that takes the grid, current position (x, y), and the dimensions of the grid (n, m).
2. If the current position is out of bounds or contains no gold, return 0.
3. Collect the gold from the current cell and mark it as visited.
4. Explore all four possible directions (up, down, left, right) recursively.
5. Return the maximum gold collected from any path starting from the current cell.
6. Iterate over all cells in the grid, starting from a cell with gold, and use the DFS function to find the maximum gold path.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n * m * 4^k) where n and m are the dimensions of the grid, and k is the maximum depth of the recursion tree.` | `O(n * m) for the visited array and the recursion stack.` |

## 🏷️ Tags

`dfs` `backtracking` `grid` `maximum`

<details>
<summary>💻 View solution</summary>

```python
'''class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        diri = [(-1,0),(0,-1),(0,1),(1,0)]
        visited = [([False]*(len(grid[0]))) for _ in range(len(grid))]
        maxi = 0

        def visit(grid,i,j,maxi):
            for k,l in diri:
                x,y = i+k,j+l
                if x>0 and x<len(grid) and y > 0 and y<len(grid[0]):
                    if grid[x][y] != 0 and not visited[x][y]:
                        maxi+=grid[x][y]
                        visited[x][y] = True
                        print(x,y)
                        visit(grid,x,y,maxi)
                        maxi-=grid[x][y]
                        visited[x][y] = False
            return maxi
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    maxi = max(maxi,visit(grid,maxi,i,j))
        return maxi
'''
class Solution:
    roww = [1, -1, 0, 0]
    coll = [0, 0, -1, 1]

    def dfs(self, grid, x, y, n, m):
        if x < 0 or x >= n or y < 0 or y >= m or grid[x][y] == 0:
            return 0
        
        curr = grid[x][y]
        grid[x][y] = 0
        localMaxGold = curr

        for i in range(4):
            newX = x + self.roww[i]
            newY = y + self.coll[i]
            localMaxGold = max(localMaxGold, curr + self.dfs(grid, newX, newY, n, m))

        grid[x][y] = curr
        return localMaxGold

    def getMaximumGold(self, grid):
        n = len(grid)
        m = len(grid[0])
        maxGold = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0:
                    maxGold = max(maxGold, self.dfs(grid, i, j, n, m))

        return maxGold


```

</details>
