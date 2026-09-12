# 🔵 1877A — Goals of Victory

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/1877/A) &nbsp;|&nbsp; **Solved:** 2026-08-15

---

## 📝 Summary

Given an array of integers, find the sum of all elements and print the negative of that sum.

## 🔍 Key Observation

The key insight is to calculate the sum of the array and then print its negative.

## ⚙️ Algorithm

1. Read the number of test cases 't'.
2. For each test case:
   a. Read the number of elements 'n' in the array.
   b. Read the array elements into a list 'arr'.
   c. Calculate the sum of all elements in 'arr' using the built-in sum function.
   d. Print the negative of the sum.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to the single pass through the array to calculate the sum.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`easy` `python` `sum` `negative`

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
    print(-sum(arr))


```

</details>
