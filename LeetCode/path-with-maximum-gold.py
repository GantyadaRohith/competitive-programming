'''class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        diri = [(-1,0),(0,-1),(0,1),(1,0)]
        visited = [([False]*(len(grid[0]))) for _ in range(len(grid))]
        maxi = 0

        def visit(grid,i,j,maxi):
            for k,l in diri:
                x,y = i+k,j+l
                if x>0 and x<len(grid) and y > 0 and y<len(grid[0]):
                    if grid[x][y] != 0 and not visited[x][y]:
                        maxi+=grid[x][y]
                        visited[x][y] = True
                        print(x,y)
                        visit(grid,x,y,maxi)
                        maxi-=grid[x][y]
                        visited[x][y] = False
            return maxi
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    maxi = max(maxi,visit(grid,maxi,i,j))
        return maxi
'''
class Solution:
    roww = [1, -1, 0, 0]
    coll = [0, 0, -1, 1]

    def dfs(self, grid, x, y, n, m):
        if x < 0 or x >= n or y < 0 or y >= m or grid[x][y] == 0:
            return 0
        
        curr = grid[x][y]
        grid[x][y] = 0
        localMaxGold = curr

        for i in range(4):
            newX = x + self.roww[i]
            newY = y + self.coll[i]
            localMaxGold = max(localMaxGold, curr + self.dfs(grid, newX, newY, n, m))

        grid[x][y] = curr
        return localMaxGold

    def getMaximumGold(self, grid):
        n = len(grid)
        m = len(grid[0])
        maxGold = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0:
                    maxGold = max(maxGold, self.dfs(grid, i, j, n, m))

        return maxGold

