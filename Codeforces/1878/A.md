# 🔵 1878A — How Much Does Daytona Cost?

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/1878/A) &nbsp;|&nbsp; **Solved:** 2026-08-16

---

## 📝 Summary

Given a list of integers and a target integer, determine if the target integer appears at least once in the list.

## 🔍 Key Observation

The key insight is to use a dictionary to count occurrences of each integer efficiently.

## ⚙️ Algorithm

1. Initialize an empty dictionary `a` to store the count of each integer in the list.
2. Iterate through the list `arr` and update the count of each integer in the dictionary `a`.
3. Check if the target integer `k` is present in the dictionary `a` and has a count of at least 1.
4. Print 'YES' if the target integer is found, otherwise print 'NO'.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to a single pass through the list.` | `O(n) for the dictionary `a`.` |

## 🏷️ Tags

`short` `lowercase` `problem` `solving`

<details>
<summary>💻 View solution</summary>

```python
import sys
input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def invr():
    return(map(int,input().split()))
def inlt():
    return(list(map(int,input().split())))

t = inp()
for _ in range(t):
    n,k = invr()
    arr = inlt()
    a = {}
    a[k] = 0
    for i in arr:
        a[i] = a.get(i,0)+1
    if a[k] >= 1:
        print("YES")
    else:
        print("NO")
```

</details>
