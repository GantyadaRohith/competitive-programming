# 🟠 surrounded-regions — Surrounded Regions

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/surrounded-regions/) &nbsp;|&nbsp; **Solved:** 2026-03-02

---

## 📝 Summary

Given a 2D board containing 'X' and 'O', capture all 'O's that are surrounded by 'X's.

## 🔍 Key Observation

The key insight is to use a depth-first search (DFS) to mark all 'O's that are connected to the border as 'T' (temporary). Then, flip all remaining 'O's to 'X' and revert the 'T's back to 'O'.

## ⚙️ Algorithm

1. Traverse the border of the board and mark all 'O's connected to the border as 'T' using DFS.
2. Traverse the entire board and flip all 'O's to 'X'.
3. Traverse the entire board again and revert all 'T's back to 'O'.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n * m) where n is the number of rows and m is the number of columns.` | `O(n * m) due to the temporary board and the recursion stack.` |

## 🏷️ Tags

`dfs` `bfs` `board` `surrounded-regions`

<details>
<summary>💻 View solution</summary>

```python
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
```

</details>
