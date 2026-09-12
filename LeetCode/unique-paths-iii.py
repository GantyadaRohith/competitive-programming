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