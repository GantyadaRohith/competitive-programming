class Solution:
    def dfs(self,r, c,ROWS,COLS,visited,board):
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        if r < 0 or c < 0 or r >= ROWS or c >= COLS:
            return
        if visited[r][c] or board[r][c] == 'X':
            return
        visited[r][c] = True
        for dr, dc in dirs:
            self.dfs(r + dr, c + dc,ROWS,COLS,visited,board)
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        temp_board = [[False]*len(board[0]) for _ in range(len(board))]
        queue = deque([])
        ROWS,COLS = len(board),len(board[0])
        for r in range(ROWS):
            if board[r][0] == 'O':
                self.dfs(r, 0,ROWS,COLS,temp_board,board)
            if board[r][COLS-1] == 'O':
                self.dfs(r, COLS-1,ROWS,COLS,temp_board,board)

        for c in range(COLS):
            if board[0][c] == 'O':
                self.dfs(0, c,ROWS,COLS,temp_board,board)
            if board[ROWS-1][c] == 'O':
                self.dfs(ROWS-1, c,ROWS,COLS,temp_board,board)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O' and not temp_board[r][c]:
                    board[r][c] = 'X'