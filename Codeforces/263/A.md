# 🔵 263A — Beautiful Matrix

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/263/A) &nbsp;|&nbsp; **Solved:** 2026-08-14

---

## 📝 Summary

Given a 5x5 matrix, find the minimum Manhattan distance from the cell containing the number 1 to the center cell.

## 🔍 Key Observation

The Manhattan distance is the sum of the absolute differences of the row and column indices of the target cell and the center cell.

## ⚙️ Algorithm

1. Read the 5x5 matrix from input, storing it in a list of lists.
2. Iterate through the matrix to find the cell containing the number 1.
3. Calculate the Manhattan distance from the found cell to the center cell (2,2).
4. Print the calculated distance.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n^2) due to the nested loops that iterate through the matrix.` | `O(1) auxiliary space, as only a few variables are used.` |

## 🏷️ Tags

`implementation` `short`

<details>
<summary>💻 View solution</summary>

```python
a = []
for i in range(5):
    a.append(list(map(int,input().split())))
i,j = 0,0
for k in range(5):
    for l in range(5):
        if a[k][l] == 1:
            i,j = k,l
            break
cnt = abs(i-2)+abs(j-2)
print(cnt) 
```

</details>
