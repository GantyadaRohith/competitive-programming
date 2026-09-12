# 🟠 stone-game — Stone Game

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/stone-game/) &nbsp;|&nbsp; **Solved:** 2026-08-02

---

## 📝 Summary

Given an array of stones, two players take turns removing stones from the end or beginning of the array. The player who removes the last stone wins.

## 🔍 Key Observation

The key insight is to use dynamic programming to calculate the maximum difference in stone values between the two players.

## ⚙️ Algorithm

The algorithm uses a recursive function `solve(l, r)` that calculates the maximum difference in stone values for the subarray `piles[l:r+1]`. It stores results in a memoization dictionary to avoid redundant calculations. The function returns the difference between the maximum value of removing the first or last stone and the result of the recursive call on the remaining subarray. The final result is compared to zero to determine if the first player can win.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n^2) due to the nested loops and memoization.` | `O(n^2) for the memoization dictionary.` |

## 🏷️ Tags

`dp` `memoization` `game theory`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = {}
        def solve(l, r):
            if l > r:
                return 0
            if memo.get((l,r),0):
                return memo[(l,r)]
            left = piles[l] - solve(l + 1, r)
            right = piles[r] - solve(l, r - 1)
            memo[(l,r)] = max(left,right)
            return memo[(l,r)]
            
        a = solve(0,len(piles)-1) 
        if a>=0:
            return True
        else:
            return False 
```

</details>
