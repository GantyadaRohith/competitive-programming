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