# 🔵 1783A — Make it Beautiful

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/1783/A) &nbsp;|&nbsp; **Solved:** 2026-08-15

---

## 📝 Summary

The problem asks to reorder a given array `a` into a new array `b` such that for any `k` from `1` to `n-1`, the sum of the first `k` elements of `b` is not equal to `b_{k+1}`. If such an array `b` can be formed, output "YES" and one such arrangement; otherwise, output "NO".

## 🔍 Key Observation

A solution is possible if and only if not all elements in the input array are identical. If a solution exists, one can be constructed by sorting the array in descending order. For positive array elements, the sum `b_1 + ... + b_k` will be strictly greater than `b_{k+1}` for `k > 1`. The only problematic case is `b_1 == b_2`, which can be resolved by swapping `b_2` with `b_n` (the smallest element) to ensure `b_1 != b_2`.

## ⚙️ Algorithm

**Constructive algorithm using sorting.**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log n)` | `O(n)` |

## 🏷️ Tags

`constructive algorithms` `sorting` `greedy` `arrays`

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
    ar1 = sorted(arr,reverse=True)
    if arr==ar1:
        print('NO')
    else:
        for i in range(1,n):
            if sum(ar1[:i]) == ar1[i]:
                ar1[i],ar1[-1] = ar1[-1],ar1[i]
        print("YES")
        print(*ar1)
```

</details>
