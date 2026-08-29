# 🔵 2218B — The 67th 6-7 Integer Problem

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/2218/B) &nbsp;|&nbsp; **Solved:** 2026-08-16

---

## 📝 Summary

Accepted solution for The 67th 6-7 Integer Problem on Codeforces.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Recursion + Sorting**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^2) (estimated -- 2 nested loops)` | `~O(1) (estimated)` |

## 🏷️ Tags

`greedy` `math` `recursion` `sorting`

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

t = inp()
for _ in range(t):
    arr = inlt()
    arr.sort(reverse=True)
    s = arr[0]
    for i in range(1,len(arr)):
        s-=arr[i]
    print(s)
```

</details>
