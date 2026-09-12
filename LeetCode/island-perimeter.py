class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row,cols = len(grid),len(grid[0])
        d = [(1,0),(-1,0),(0,1),(0,-1)]
        cnt = 0
        visited = [[False for _ in range(cols)] for _ in range(row)]
        def dfs(r,c):
            nonlocal cnt
            if r<0 or r>=row or c<0 or c>=cols:
                cnt+=1
                return
            if grid[r][c] != 1:
                cnt+=1
                return
            if visited[r][c]:
                return 
            visited[r][c] = True
            for dr,dc in d:
                dfs(r+dr,c+dc)
        for i in range(row):
            for j in range(cols):
                if grid[i][j] == 1:
                    dfs(i,j)
                    break
        return cnt
                
        