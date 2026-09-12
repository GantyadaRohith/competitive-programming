# 🔵 510A — Fox And Snake

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/510/A) &nbsp;|&nbsp; **Solved:** 2026-08-25

---

## 📝 Summary

Print an m x n grid representing a "snake" pattern where odd-indexed rows are filled with '#' characters, and even-indexed rows alternate between having a single '#' at the rightmost column and a single '#' at the leftmost column.

## 🔍 Key Observation

The pattern is regular and depends on the row index's parity. Even rows are solid, while odd rows require a flag to alternate the '#' position between the left and right edges.

## ⚙️ Algorithm

**Direct Implementation / Pattern Generation**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(m * n)` | `O(n)` |

## 🏷️ Tags

`implementation` `strings` `patterns` `loops` `adhoc`

<details>
<summary>💻 View solution</summary>

```python
m,n = map(int,input().split())
s = '#'*n
t1 = '.'*(n-1)+'#'
t2 = '#'+'.'*(n-1)
f = 0
for i in range(m):
    if i%2 == 0:
        print(s)
    elif f == 0:
        f = 1
        print(t1)
    else:
        f = 0
        print(t2)
```

</details>
