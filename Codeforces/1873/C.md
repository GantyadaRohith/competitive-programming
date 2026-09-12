# 🔵 1873C — Target Practice

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/1873/C) &nbsp;|&nbsp; **Solved:** 2026-08-15

---

## 📝 Summary

Given a 10x10 grid of characters, calculate the total points based on the positions of 'X' characters, where points are determined by the layer of the grid they are in.

## 🔍 Key Observation

The key insight is to calculate the layer of each 'X' based on its position in the grid.

## ⚙️ Algorithm

1. Read the input for the number of test cases (t).
2. For each test case, read the 10x10 grid of characters.
3. Initialize a variable `pts` to store the total points.
4. Iterate over each cell in the grid.
5. For each 'X' character, calculate its layer as the minimum of its row and column indices, plus one.
6. Add the layer to `pts`.
7. Print the total points for the test case.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(t * 100) due to the nested loops iterating over the grid for each test case.` | `O(1) auxiliary space as only a few variables are used.` |

## 🏷️ Tags

`short` `lowercase` `grid` `points` `layer`

<details>
<summary>💻 View solution</summary>

```python
import sys
input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))

t = inp()
for _ in range(t):
    a = []
    for _ in range(10):
        a.append(input())
    pts = 0
    for i in range(10):
        for j in range(10): 
            layer = min(i, j, 9-i, 9-j) + 1
            if a[i][j] == 'X':
                pts+=layer
    print(pts)

```

</details>
