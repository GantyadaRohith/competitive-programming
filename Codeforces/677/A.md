# 🔵 677A — Vanya and Fence

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/677/A) &nbsp;|&nbsp; **Solved:** 2026-08-20

---

## 📝 Summary

Calculate the minimum total width required for 'n' friends to pass a fence of height 'h', where friends taller than 'h' require 2 units of width and others require 1 unit.

## 🔍 Key Observation

The width contribution of each person is determined by a simple conditional rule: 2 units if their height exceeds the fence height 'h', otherwise 1 unit.

## ⚙️ Algorithm

**Iteration / Direct Simulation**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n)` | `O(n)` |

## 🏷️ Tags

`implementation` `arrays` `ad-hoc` `easy`

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

n,h = invr()
arr = inlt()
width = 0
for i in arr:
    if i > h:
        width+=2
    else:
        width+=1
print(width)
```

</details>
