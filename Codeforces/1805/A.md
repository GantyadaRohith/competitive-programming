# 🔵 1805A — We Need the Zero

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/1805/A) &nbsp;|&nbsp; **Solved:** 2026-08-14

---

## 📝 Summary

Given an array of integers, find the XOR of all elements. If the array length is odd, print the XOR. If even, print 0 if all elements are 0, otherwise print -1.

## 🔍 Key Observation

The XOR of all elements in an array is zero if and only if all elements are zero.

## ⚙️ Algorithm

1. Initialize a variable `x` to the first element of the array.
2. Iterate through the array starting from the second element, updating `x` with the XOR of `x` and the current element.
3. If the array length is odd, print `x`.
4. If the array length is even, check if `x` is zero. If so, print 0; otherwise, print -1.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to a single pass through the array.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`bitmasks` `brute force`

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
    a = inlt()
    x = a[0]
    for i in range(1,n):
        x^=a[i]
    if n&1:
        print(x)
    else:
        if x == 0:
            print(0)
        else:
            print(-1)


```

</details>
