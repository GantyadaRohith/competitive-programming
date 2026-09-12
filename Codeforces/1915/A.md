# 🔵 1915A — Odd One Out

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/1915/A) &nbsp;|&nbsp; **Solved:** 2026-08-21

---

## 📝 Summary

Given an array of integers, find the integer that appears an odd number of times.

## 🔍 Key Observation

The XOR operation can be used to find the odd one out because it cancels out pairs of identical numbers.

## ⚙️ Algorithm

1. Initialize a variable `cnt` to 0.
2. Iterate through each number in the array.
3. For each number, XOR it with `cnt`.
4. After processing all numbers, `cnt` will hold the odd one out.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to a single pass through the array.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`bitwise` `xor` `single`

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
