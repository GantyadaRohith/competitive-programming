# 🔵 2259A — Moo Language School

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/2259/A) &nbsp;|&nbsp; **Solved:** 2026-09-05

---

## 📝 Summary

Given a list of integers and a divisor, count how many sublists of length k contain at least one zero.

## 🔍 Key Observation

The key insight is to use a sliding window approach to efficiently count sublists containing at least one zero.

## ⚙️ Algorithm

1. Initialize a counter `cnt` to zero.
2. Iterate over the list in steps of `k`.
3. For each sublist of length `k`, check if it contains at least one zero.
4. If it does, increment the counter `cnt`.
5. Print the final count.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to a single pass through the list.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`sliding window` `sublist` `zero count`

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
