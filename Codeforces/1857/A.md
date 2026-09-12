# 🔵 1857A — Array Coloring

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/1857/A) &nbsp;|&nbsp; **Solved:** 2026-08-15

---

## 📝 Summary

Given an array of integers, determine if it's possible to color all elements with two colors such that no two adjacent elements have the same color.

## 🔍 Key Observation

The problem can be solved by counting the number of odd numbers in the array. If the count of odd numbers is even, it's possible to color the array as required.

## ⚙️ Algorithm

1. Count the number of odd numbers in the array.
2. If the count of odd numbers is even, print 'YES'.
3. If the count of odd numbers is odd, print 'NO'.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to a single pass through the array.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`array` `odd` `even` `coloring`

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
