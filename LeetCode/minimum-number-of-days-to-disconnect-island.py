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