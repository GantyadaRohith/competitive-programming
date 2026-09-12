class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        row,cols = len(image),len(image[0])
        old_color = image[sr][sc]
        d = [(1,0),(-1,0),(0,1),(0,-1)]
        if old_color == color:
            return image
        def dfs(r,c):
            if r<0 or r>=row or c<0 or c>=cols:
                return
            if image[r][c] != old_color:
                return
            image[r][c] = color
            for dr,dc in d:
                dfs(r+dr,c+dc)
        dfs(sr,sc)
        return image