# 🟠 pascals-triangle-ii — Pascal's Triangle II

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/pascals-triangle-ii/) &nbsp;|&nbsp; **Solved:** 2026-08-09

---

## 📝 Summary

Given a non-negative integer rowIndex, return the rowIndex-th row of Pascal's Triangle.

## 🔍 Key Observation

The problem can be solved using dynamic programming to efficiently generate the row without recalculating previous rows.

## ⚙️ Algorithm

1. Initialize the first two rows of Pascal's Triangle: [1] and [1,1].
2. For each subsequent row, start and end with 1.
3. For each element in the middle of the row, calculate its value as the sum of the two elements directly above it from the previous row.
4. Append the row to the list of rows and return the rowIndex-th row.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n^2) due to the nested loops that generate each row.` | `O(n^2) for storing all rows of Pascal's Triangle.` |

## 🏷️ Tags

`dynamic programming` `pascal's triangle` `triangle`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
            n = 34
            a = [[1],[1,1]]
            n-=2
            for i in range(1,n+1):
                a.append([1])
                for j in range(1,len(a[-2])):
                    a[-1].append(a[-2][j-1]+a[-2][j])
                a[-1].append(1)
            return a[rowIndex]      
```

</details>
