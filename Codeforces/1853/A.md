# 🔵 1853A — Desorting

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/1853/A) &nbsp;|&nbsp; **Solved:** 2026-08-15

---

## 📝 Summary

The problem asks for the minimum non-negative integer k such that by changing each element a_x to either a_x-k or a_x+k, the resulting array is no longer sorted non-decreasingly (i.e., there exists at least one index i where a_i > a_{i+1}).

## 🔍 Key Observation

To make a_i > a_{i+1} using the smallest k for a specific pair, we should apply +k to a_i and -k to a_{i+1}. This requires a_i + k > a_{i+1} - k, which simplifies to 2k > a_{i+1} - a_i. The smallest integer k satisfying this is ( (a_{i+1} - a_i) // 2 ) + 1. The overall minimum k is achieved by finding the minimum difference (a_{i+1} - a_i) across all adjacent pairs in the original array. If the array is already desorted, k=0.

## ⚙️ Algorithm

**Iterate through the array to find the minimum difference between adjacent elements, say min_diff = min(arr[i] - arr[i-1]). If min_diff is negative, the array is already desorted, and the answer is 0. Otherwise, the answer is (min_diff // 2) + 1.**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n)` | `O(n)` |

## 🏷️ Tags

`greedy` `arrays` `math`

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
    mini = 10**9+1
    for i in range(1,len(arr)):
        if mini > (arr[i]-arr[i-1]):
            mini = arr[i]-arr[i-1]
    if mini>=0:
        print((mini//2)+1)
    else:
        print(0)
```

</details>
