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
            