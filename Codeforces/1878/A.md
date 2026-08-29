# 🔵 1878A — How Much Does Daytona Cost?

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/1878/A) &nbsp;|&nbsp; **Solved:** 2026-08-16

---

## 📝 Summary

Accepted solution for How Much Does Daytona Cost? on Codeforces.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Recursion**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n) (estimated)` | `~O(1) (estimated)` |

## 🏷️ Tags

`greedy` `recursion`

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
