# 🟠 delete-greatest-value-in-each-row — Delete Greatest Value in Each Row

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/delete-greatest-value-in-each-row/) &nbsp;|&nbsp; **Solved:** 2026-07-17

---

## 📝 Summary

Given a matrix of integers, delete the greatest value in each row and return the sum of the remaining values.

## 🔍 Key Observation

Sorting each row allows the greatest value to be easily identified and removed.

## ⚙️ Algorithm

1. Sort each row of the matrix in ascending order.
2. For each column, find the maximum value.
3. Sum these maximum values to get the result.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log n) due to sorting each row.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`sort` `row` `max` `sum`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for row in grid:
            row.sort()

        return sum(max(col) for col in zip(*grid))
```

</details>
