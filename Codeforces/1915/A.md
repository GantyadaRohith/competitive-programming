# 🔵 1915A — Odd One Out

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/1915/A) &nbsp;|&nbsp; **Solved:** 2026-08-21

---

## 📝 Summary

Given three integers where exactly two are identical, the problem asks to find the value of the unique integer.

## 🔍 Key Observation

The bitwise XOR sum of a set of numbers where one number appears once and all other numbers appear an even number of times will result in the unique number itself. For three numbers `a, a, b`, `a ^ a ^ b = b`.

## ⚙️ Algorithm

**Bitwise XOR**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(t)` | `O(1)` |

## 🏷️ Tags

`bitwise operations` `xor` `implementation`

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
    arr = inlt()
    cnt = 0
    for i in arr:
        cnt^=i
    print(cnt)
```

</details>
