# 🟠 dungeon-game — Dungeon Game

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/dungeon-game/) &nbsp;|&nbsp; **Solved:** 2026-03-07

---

## 📝 Summary

Given a 2D dungeon with negative health points, find the minimum initial health required to survive the dungeon.

## 🔍 Key Observation

The solution uses dynamic programming to calculate the minimum health needed at each cell, ensuring survival.

## ⚙️ Algorithm

The algorithm iterates over the dungeon from the bottom-right corner to the top-left corner. It calculates the minimum health required to reach each cell by considering the minimum health required from the cell below and to the right. The initial health required is determined by the maximum of 1 and the difference between the current cell's health and the minimum health required to reach it.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(m * n) due to the nested loops iterating over the dungeon.` | `O(m * n) for the dp array used to store intermediate results.` |

## 🏷️ Tags

`dp` `min-health` `dungeon`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m,n=len(dungeon),len(dungeon[0])
        dp=[[0]*n for _ in range(m)]
        dp[m-1][n-1] = max(1, 1 - dungeon[m-1][n-1])
        for i in range(m-2,-1,-1):
            need = dp[i+1][n-1]
            dp[i][n-1] = max(1, need - dungeon[i][n-1])
        for j in range(n-2,-1,-1):
            need = dp[m-1][j+1]
            dp[m-1][j] = max(1, need - dungeon[m-1][j])
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                need = min(dp[i+1][j], dp[i][j+1])
                dp[i][j] = max(1, need - dungeon[i][j])
        return dp[0][0]
```

</details>
