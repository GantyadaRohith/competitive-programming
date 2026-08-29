# 🔵 1873C — Target Practice

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/1873/C) &nbsp;|&nbsp; **Solved:** 2026-08-15

---

## 📝 Summary

The problem asks to calculate the total score from 'X's on a 10x10 target grid. Each 'X' contributes points corresponding to its concentric "ring" number, where the outermost ring scores 1 point and points increase towards the center.

## 🔍 Key Observation

The point value for a cell `(i, j)` is directly determined by its minimum distance to any of the four borders (top, left, bottom, right), plus one. This can be calculated with the formula `min(i, j, 9-i, 9-j) + 1`.

## ⚙️ Algorithm

**Direct simulation / Implementation**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(1)` | `O(1)` |

## 🏷️ Tags

`implementation` `math` `grids` `ad hoc`

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
