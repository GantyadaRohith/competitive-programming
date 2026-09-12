class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        out = []
        for j in range(len(grid[0])):
            maxlen=0
            for i in range(len(grid)):
                if grid[i][j] == 0:
                    maxlen = max(maxlen,1)
                elif grid[i][j]<0:
                    maxlen = max(maxlen,math.floor(math.log10(-grid[i][j]))+2)
                    print(maxlen)
                else:
                    maxlen = max(maxlen,math.floor(math.log10(grid[i][j]))+1)
                    print(maxlen)
            out.append(maxlen)
        return out