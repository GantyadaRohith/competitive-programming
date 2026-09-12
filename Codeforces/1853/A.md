# 🔵 1853A — Desorting

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/1853/A) &nbsp;|&nbsp; **Solved:** 2026-08-15

---

## 📝 Summary

Given an array of integers, find the minimum difference between any two consecutive elements and print the number of ways to make the array sorted by swapping at most one pair of adjacent elements.

## 🔍 Key Observation

The key insight is to identify the minimum difference between consecutive elements and determine how many swaps are needed to sort the array by swapping at most one pair of adjacent elements.

## ⚙️ Algorithm

1. Iterate through the array to find the minimum difference between consecutive elements.
2. If the minimum difference is non-negative, calculate the number of swaps needed to sort the array by swapping at most one pair of adjacent elements.
3. If the minimum difference is negative, it's impossible to sort the array by swapping at most one pair of adjacent elements, so print 0.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to a single pass through the array.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`short` `lowercase` `algorithm` `sorting`

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
