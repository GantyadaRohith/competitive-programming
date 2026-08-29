# 🔵 546A — Soldier and Bananas

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/546/A) &nbsp;|&nbsp; **Solved:** 2026-08-20

---

## 📝 Summary

Accepted solution for Soldier and Bananas on Codeforces.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Recursion**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n) (estimated)` | `~O(1) (estimated)` |

## 🏷️ Tags

`brute force` `implementation` `math` `recursion`

<details>
<summary>💻 View solution</summary>

```python
import sys
input = sys.stdin.readline
def invr():
    return(map(int,input().split()))

k,n,w = invr()
su = (w*(w+1))/2
to = su*k
if to >= n:
    print(int(to-n))
else:
    print(0)
```

</details>
