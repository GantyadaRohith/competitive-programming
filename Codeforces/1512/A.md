# 🔵 1512A — Spy Detected!

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/1512/A) &nbsp;|&nbsp; **Solved:** 2026-08-21

---

## 📝 Summary

Given an array of integers, find the first element that appears exactly once.

## 🔍 Key Observation

The key insight is to use two dictionaries to count occurrences and their first appearance index.

## ⚙️ Algorithm

1. Initialize two dictionaries, `a` and `b`, to store the first appearance index and count of each element, respectively.
2. Iterate through the array, updating `a` and `b` for each element.
3. After processing the array, iterate through `b` to find the first element with a count of 1 and print its first appearance index.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to a single pass through the array and a second pass through the dictionary.` | `O(n) for the two dictionaries.` |

## 🏷️ Tags

`python` `hashmap` `dictionary`

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
    a = {}
    b = {}
    for i in range(n):
        a[arr[i]] = i
        b[arr[i]] = b.get(arr[i],0) + 1
    for i,j in b.items():
        if j == 1:
            print(a[i]+1)
            break
    
    
```

</details>
