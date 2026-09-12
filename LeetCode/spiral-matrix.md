# 🟠 spiral-matrix — Spiral Matrix

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/spiral-matrix/) &nbsp;|&nbsp; **Solved:** 2025-11-16

---

## 📝 Summary

Given a matrix, return the elements in a spiral order.

## 🔍 Key Observation

The solution uses four pointers to track the boundaries of the matrix and iterates through it in a spiral pattern.

## ⚙️ Algorithm

The algorithm uses four pointers (top, bottom, left, right) to define the boundaries of the matrix. It iterates through the matrix in a spiral order by moving right, down, left, and up, updating the pointers accordingly after each complete cycle.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n * m) where n is the number of rows and m is the number of columns in the matrix.` | `O(n * m) for storing the result.` |

## 🏷️ Tags

`python` `matrix` `spiral`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        a = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while left <= right and top <= bottom:

            # left → right
            for i in range(left, right + 1):
                a.append(matrix[top][i])
            top += 1

            # top → bottom
            for i in range(top, bottom + 1):
                a.append(matrix[i][right])
            right -= 1

            # right → left
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    a.append(matrix[bottom][i])
                bottom -= 1

            # bottom → top
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    a.append(matrix[i][left])
                left += 1

        return a

```

</details>
