# 🟠 minimum-number-of-days-to-disconnect-island — Minimum Number of Days to Disconnect Island

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/minimum-number-of-days-to-disconnect-island/) &nbsp;|&nbsp; **Solved:** 2026-03-05

---

## 📝 Summary

Given a grid representing an island, determine the minimum number of days required to disconnect the island by removing exactly one land cell.

## 🔍 Key Observation

The critical insight is to use Tarjan's algorithm to find the cut vertex in the graph formed by the land cells, which represents the minimum number of days required to disconnect the island.

## ⚙️ Algorithm

1. Count the number of islands and land cells in the grid.
2. If there is more than one island, return 0 as it is already disconnected.
3. If there is only one island and it is a single land cell, return 1 as it can be disconnected in one day.
4. Use Tarjan's algorithm to find the cut vertex in the graph formed by the land cells.
5. Return 1 if a cut vertex is found, otherwise return 2.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(m * n) due to the traversal of the grid and the DFS in Tarjan's algorithm.` | `O(m * n) for storing the grid, disc, and low arrays.` |

## 🏷️ Tags

`graph` `tarjan` `disjoint-set` `island` `cut-vertex`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def minDays(self, grid):
        m, n = len(grid), len(grid[0])
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        def neighbors(r, c):
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                    yield nr, nc

        # Count islands + land cells
        def count_islands():
            seen = set()
            islands = 0
            land = 0

            def dfs(r, c):
                stack = [(r, c)]
                seen.add((r, c))
                while stack:
                    x, y = stack.pop()
                    for nx, ny in neighbors(x, y):
                        if (nx, ny) not in seen:
                            seen.add((nx, ny))
                            stack.append((nx, ny))

            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1:
                        land += 1
                        if (i, j) not in seen:
                            islands += 1
                            dfs(i, j)

            return islands, land

        islands, land = count_islands()

        if islands != 1:
            return 0

        # ⭐ critical edge case
        if land == 1:
            return 1

        disc = {}
        low = {}
        time = 0
        found_cut = False

        start = None
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start = (i, j)
                    break
            if start:
                break

        def tarjan(r, c, parent):
            nonlocal time, found_cut
            disc[(r, c)] = low[(r, c)] = time
            time += 1

            children = 0

            for nr, nc in neighbors(r, c):
                if (nr, nc) == parent:
                    continue

                if (nr, nc) not in disc:
                    children += 1
                    tarjan(nr, nc, (r, c))
                    low[(r, c)] = min(low[(r, c)], low[(nr, nc)])

                    if parent is not None and low[(nr, nc)] >= disc[(r, c)]:
                        found_cut = True
                else:
                    low[(r, c)] = min(low[(r, c)], disc[(nr, nc)])

            if parent is None and children > 1:
                found_cut = True

        tarjan(start[0], start[1], None)

        return 1 if found_cut else 2
```

</details>
