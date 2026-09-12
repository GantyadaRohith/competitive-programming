# 🟠 rotting-oranges — Rotting Oranges

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/rotting-oranges/) &nbsp;|&nbsp; **Solved:** 2026-05-01

---

## 📝 Summary

Given a grid representing a 2D array of oranges, where 0 represents an empty cell, 1 represents a fresh orange, and 2 represents a rotten orange, determine the minimum time required for all oranges to rot. If it's impossible for all oranges to rot, return -1.

## 🔍 Key Observation

The key insight is to use a breadth-first search (BFS) to simulate the rotting process, ensuring that oranges rot in the order they are added to the queue.

## ⚙️ Algorithm

1. Initialize a queue with all rotten oranges and mark them as visited. Also, initialize a distance matrix to keep track of the time each orange takes to rot.
2. Use BFS to process each rotten orange, marking its neighbors as rotten and updating their distance.
3. Continue the process until the queue is empty.
4. After processing, check if any fresh oranges remain. If so, return -1. Otherwise, return the maximum time recorded.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(m * n) where m is the number of rows and n is the number of columns, as each cell is processed once.` | `O(m * n) for the queue and the visited matrix.` |

## 🏷️ Tags

`bfs` `queue` `grid` `rotting`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        distance = [[0 for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i, j))
                    visited[i][j] = True
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols:
                    if grid[nx][ny] == 1 and not visited[nx][ny]:
                        visited[nx][ny] = True
                        grid[nx][ny] = 2  # Orange becomes rotten
                        distance[nx][ny] = distance[x][y] + 1
                        queue.append((nx, ny))
        max_time = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1
                max_time = max(max_time, distance[i][j])

        return max_time
```

</details>
