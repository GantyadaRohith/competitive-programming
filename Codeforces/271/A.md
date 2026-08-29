# 🔵 271A — Beautiful Year

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/271/A) &nbsp;|&nbsp; **Solved:** 2026-08-20

---

## 📝 Summary

Accepted solution for Beautiful Year on Codeforces.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Recursion + Hash map/set lookup**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n^2) (estimated -- 2 nested loops)` | `~O(n) (estimated)` |

## 🏷️ Tags

`brute force` `recursion` `hash-map`

<details>
<summary>💻 View solution</summary>

```python
import sys
input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp():
    return(int(input()))

year = inp()
for i in range(year+1,9013):
    s = set()
    n = 0
    for j in str(i):
        if j not in s:
            s.add(j)
            n+=1
        else:
            break
    if n == 4:
        print(i)
        break
```

</details>
