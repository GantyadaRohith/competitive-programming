class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row,cols = len(grid),len(grid[0])
        dir = [(1,0),(-1,0),(0,1),(0,-1)]
        visited = [[False]*cols for _ in range(row)]
        cnt = 0
        def dfs(l,r):
            if l<0 or l>=len(grid) or r<0 or r>=len(grid[0]) :
                return 
            if visited[l][r] or grid[l][r] == '0':
                return
            visited[l][r] = True
            for dr,dc in dir:
                dfs(l+dr,r+dc)

        island = 0
        for r in range(row):
            for c in range(cols):
                if grid[r][c] == '1' and not visited[r][c]:
                    dfs(r,c)
                    cnt+=1
        return cnt