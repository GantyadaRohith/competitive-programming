# 🔵 2259A — Moo Language School

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/2259/A) &nbsp;|&nbsp; **Solved:** 2026-09-05

---

## 📝 Summary

Given an array of integers and an integer `k`, count the number of non-overlapping blocks of `k` consecutive elements that do not contain the value zero.

## 🔍 Key Observation

The problem can be solved by directly iterating through the array in steps of `k` and checking each resulting block of `k` elements independently for the absence of zero.

## ⚙️ Algorithm

**Direct iteration / Block processing**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n)` | `O(n)` |

## 🏷️ Tags

`arrays` `counting` `brute force` `simulation`

<details>
<summary>💻 View solution</summary>

```python
import sys
input = sys.stdin.readline
 
############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().strip())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))
 
t = inp()
for _ in range(t):
    n,k = invr()
    arr = inlt()
    cnt = 0
    for i in range(0, n, k):
        x = arr[i:i+k]
        if 0 not in x:
            cnt+=1
    print(cnt)
```

</details>
