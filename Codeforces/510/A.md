# 🔵 510A — Fox And Snake

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/510/A) &nbsp;|&nbsp; **Solved:** 2026-08-25

---

## 📝 Summary

Given a grid size m x n, print a pattern of '#' and '.' characters in a snake-like pattern.

## 🔍 Key Observation

The pattern alternates between two lines of '#' and '.' characters.

## ⚙️ Algorithm

The solution uses a simple loop to iterate over the grid rows. It checks if the row index is even or odd to determine which pattern to print. The pattern alternates between two lines, '#' and '.'.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(m) due to the single loop over the grid rows.` | `O(1) auxiliary space as only a few variables are used.` |

## 🏷️ Tags

`snake` `pattern` `alternating`

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
