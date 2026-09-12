# 🟠 shortest-path-in-binary-matrix — Shortest Path in Binary Matrix

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/shortest-path-in-binary-matrix/) &nbsp;|&nbsp; **Solved:** 2026-05-01

---

## 📝 Summary

Find the shortest path in a binary matrix with obstacles.

## 🔍 Key Observation

Use a breadth-first search (BFS) to explore all possible paths from the start to the end.

## ⚙️ Algorithm

1. Initialize a queue with the starting position (0,0) and mark it as visited by setting its value to 1.
2. Use a direction array to explore all possible moves (up, down, left, right, and diagonals).
3. For each position, check if it is within bounds and not an obstacle.
4. If the position is the end, return the distance.
5. Otherwise, mark the position as visited and add it to the queue with an incremented distance.
6. Repeat until the queue is empty or the end is reached.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n^2) due to the BFS traversal of the grid.` | `O(n^2) for the queue and grid storage.` |

## 🏷️ Tags

`short` `lowercase` `bfs` `binary matrix`

<details>
<summary>💻 View solution</summary>

```python
from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        dir = [(0,1),(1,0),(1,1),(-1,-1),(-1,0),(0,-1),(1,-1),(-1,1)]
        r,c = len(grid),len(grid[0])
        if grid[0][0] or grid[-1][-1]:
            return -1
        q = deque([(0,0)])
        grid[0][0] = 1

        while q:
            rw,cl = q.popleft()
            d = grid[rw][cl]
            if (rw,cl) == (r-1,c-1):
                return d
            for dr in (-1,0,1):
                for dc in (-1,0,1):
                    if dr or dc:
                        nr,nc = rw+dr,cl+dc
                        if 0<=nr<r and 0<=nc<c and grid[nr][nc] == 0:
                            grid[nr][nc] = d+1
                            q.append((nr,nc))
        return -1
            
```

</details>
