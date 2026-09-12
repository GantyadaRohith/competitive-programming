# 🟠 find-the-width-of-columns-of-a-grid — Find the Width of Columns of a Grid

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/find-the-width-of-columns-of-a-grid/) &nbsp;|&nbsp; **Solved:** 2026-07-17

---

## 📝 Summary

Given a 2D grid of integers, find the maximum width of each column.

## 🔍 Key Observation

The key insight is to iterate through each column and determine the maximum width of numbers in that column, considering both positive and negative numbers.

## ⚙️ Algorithm

1. Initialize an empty list `out` to store the maximum width of each column.
2. For each column index `j` from 0 to the number of columns minus 1:
   a. Initialize `maxlen` to 0.
   b. For each row index `i` from 0 to the number of rows minus 1:
      i. If the current cell is 0, set `maxlen` to 1.
      ii. If the current cell is negative, calculate the width as `math.floor(math.log10(-grid[i][j])) + 2`.
      iii. If the current cell is positive, calculate the width as `math.floor(math.log10(grid[i][j])) + 1`.
   c. Append `maxlen` to `out`.
3. Return `out`.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n * m), where n is the number of rows and m is the number of columns.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`python` `math` `logarithm` `grid`

<details>
<summary>💻 View solution</summary>

```python
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
```

</details>
