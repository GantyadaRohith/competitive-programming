# 🔵 1857A — Array Coloring

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/1857/A) &nbsp;|&nbsp; **Solved:** 2026-08-15

---

## 📝 Summary

The problem asks if an array can be partitioned into two (possibly empty) subarrays such that the sum of elements in each subarray is even.

## 🔍 Key Observation

For both subarray sums to be even, their combined sum (the total sum of the original array) must also be even. An array's total sum is even if and only if it contains an even number of odd integers. If the total sum is even, it is always possible to achieve the goal (e.g., by putting all elements into one subarray and leaving the other empty). Thus, the problem reduces to checking if the total count of odd numbers in the array is even.

## ⚙️ Algorithm

**Parity check by counting odd numbers.**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(N) per test case` | `O(N) per test case` |

## 🏷️ Tags

`math` `parity` `arrays` `implementation`

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
    odd = 0
    for i in arr:
        if i&1:
            odd+=1
    if odd&1:
        print('NO')
    else:
        print('YES')
```

</details>
