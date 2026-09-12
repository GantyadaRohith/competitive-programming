# 🟠 row-with-maximum-ones — Row With Maximum Ones

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/row-with-maximum-ones/) &nbsp;|&nbsp; **Solved:** 2026-07-17

---

## 📝 Summary

Given a binary matrix, find the row with the maximum number of ones.

## 🔍 Key Observation

The problem can be solved efficiently by counting the ones in each row and keeping track of the row with the highest count.

## ⚙️ Algorithm

1. Initialize an empty dictionary `out` to store the count of ones in each row and a variable `cnt` to count ones in the current row.
2. Iterate over each row in the matrix.
3. For each row, initialize `cnt` to 0 and iterate over each element in the row.
4. If the element is 1, increment `cnt`.
5. Store the count of ones in the current row in the dictionary `out` with the row index as the key.
6. Find the maximum value in the dictionary `out` to determine the row with the maximum number of ones.
7. Return the row index and the count of ones.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n * m) where n is the number of rows and m is the number of columns in the matrix.` | `O(n) for storing the count of ones in each row.` |

## 🏷️ Tags

`python` `binary` `matrix` `counting`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        out = {}
        cnt =0
        for i in range(len(mat)):
            cnt = 0
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    cnt+=1
            out[i] = cnt
        maxi = max(list(out.values()))
        res = []
        for i,j in out.items():
            if j == maxi:
                return [int(i),int(j)]


```

</details>
