# 🔵 1742A — Sum

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/1742/A) &nbsp;|&nbsp; **Solved:** 2026-08-20

---

## 📝 Summary

Given three integers, determine if they can form a triangle.

## 🔍 Key Observation

The triangle inequality theorem states that the sum of the lengths of any two sides of a triangle must be greater than the length of the remaining side.

## ⚙️ Algorithm

The solution checks all three possible combinations of the three integers to see if they satisfy the triangle inequality theorem. If any combination satisfies the condition, it prints 'YES'; otherwise, it prints 'NO'.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(1) due to constant-time operations.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`easy` `math` `triangle`

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
    a,b,c = invr()
    if a+b == c or a+c == b or b+c == a:
        print("YES")
    else:
        print("NO")
```

</details>
