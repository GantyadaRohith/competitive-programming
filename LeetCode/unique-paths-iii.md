# 🟠 unique-paths-iii — Unique Paths III

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/unique-paths-iii/) &nbsp;|&nbsp; **Solved:** 2026-03-07

---

## 📝 Summary

Given a 2D grid representing a maze with obstacles, find the number of unique paths from the start to the end.

## 🔍 Key Observation

The solution uses depth-first search (DFS) to explore all possible paths while keeping track of visited cells and the number of steps taken.

## ⚙️ Algorithm

The algorithm initializes the grid with start and end positions, counts the number of empty cells, and uses DFS to explore all paths. It marks visited cells as -2 and unvisited cells as 0. The DFS function returns the number of unique paths from the start to the end when the number of steps matches the total number of empty cells.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(2^(m*n)) in the worst case, where m is the number of rows and n is the number of columns. This is because each cell can be visited or not visited, leading to 2^(m*n) possible paths.` | `O(m*n) due to the recursion stack and the grid itself.` |

## 🏷️ Tags

`dfs` `backtracking` `maze` `unique-paths`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        r,c = len(grid),len(grid[0])
        sx,sy = -1,-1
        ex,ey = -1,-1
        stepc = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    sx,sy = i,j
                elif grid[i][j] == 2:
                    ex,ey = i,j
                if grid[i][j] == 0:
                    stepc+=1
        def dfs(grid,i,j,ex,ey,m,n,stepc,counter):
            if i<0 or j<0 or i>m-1 or j>n-1:
                return 0
            if i == ex and j == ey:
                if stepc == counter:
                    return 1
                return 0
            temp = 0
            if grid[i][j] == -2:
                return 0
            if grid[i][j] == -1:
                return 0
            if grid[i][j] == 0:
                counter+=1
            grid[i][j] = -2
            up = dfs(grid,i-1,j,ex,ey,m,n,stepc,counter)
            down = dfs(grid,i+1,j,ex,ey,m,n,stepc,counter)
            left = dfs(grid,i,j-1,ex,ey,m,n,stepc,counter)
            right = dfs(grid,i,j+1,ex,ey,m,n,stepc,counter)
            if i == sx and j == sy:
                grid[i][j] = 1
            grid[i][j] = 0
            temp = left+down+up+right
            return temp
        return dfs(grid,sx,sy,ex,ey,r,c,stepc,0)
```

</details>
