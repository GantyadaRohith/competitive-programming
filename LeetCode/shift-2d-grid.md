# 🟠 shift-2d-grid — Shift 2D Grid

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/shift-2d-grid/) &nbsp;|&nbsp; **Solved:** 2026-07-20

---

## 📝 Summary

Given a 2D grid and an integer k, rotate the grid in place by k positions.

## 🔍 Key Observation

The problem can be solved by treating the 2D grid as a 1D array and performing a series of rotations.

## ⚙️ Algorithm

1. Convert the 2D grid into a 1D array of size r*c.
2. Perform a series of rotations on the 1D array to achieve the desired shift.
3. Convert the 1D array back into a 2D grid.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to the conversion and rotation operations.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`shift` `2d` `grid` `rotation`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        if not k: return grid
        r, c = len(grid), len(grid[0])
        n = r * c
        k %= n
        if not k: return grid

        def shift(i, j):
            while i < j:
                grid[i // c][i % c], grid[j // c][j % c] = grid[j // c][j % c], grid[i // c][i % c]
                i += 1
                j -= 1

        shift(0, n - 1)
        shift(0, k - 1)
        shift(k, n - 1)
        
        return grid
```

</details>
