# 🔵 1783A — Make it Beautiful

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/1783/A) &nbsp;|&nbsp; **Solved:** 2026-08-15

---

## 📝 Summary

Given an array, determine if it can be sorted in non-decreasing order by swapping adjacent elements.

## 🔍 Key Observation

The key insight is to check if the array can be sorted by swapping adjacent elements, which is equivalent to checking if it is possible to make the array a palindrome.

## ⚙️ Algorithm

1. Sort the array in descending order to find the largest element that can be swapped to the end to make the array non-decreasing.
2. Check if the array is already sorted in non-decreasing order.
3. If not, find the first index where the array is not in non-decreasing order and swap the element with the last element to make the array non-decreasing.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log n) due to sorting.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`sort` `palindrome` `swap`

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
