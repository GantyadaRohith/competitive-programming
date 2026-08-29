# 🔵 1512A — Spy Detected!

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/1512/A) &nbsp;|&nbsp; **Solved:** 2026-08-21

---

## 📝 Summary

The problem asks to find the 1-based index of the unique integer in an array, where all other integers appear at least twice.

## 🔍 Key Observation

Exactly one number in the array appears only once, while all other numbers appear multiple times. We can identify this unique number by counting frequencies.

## ⚙️ Algorithm

**Hash map (frequency counting)**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n)` | `O(n)` |

## 🏷️ Tags

`arrays` `hash maps` `counting` `implementation` `brute force`

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
    n = inp()
    arr = inlt()
    a = {}
    b = {}
    for i in range(n):
        a[arr[i]] = i
        b[arr[i]] = b.get(arr[i],0) + 1
    for i,j in b.items():
        if j == 1:
            print(a[i]+1)
            break
    
    
```

</details>
