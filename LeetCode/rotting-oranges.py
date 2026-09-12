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