# 🔵 1873A — Short Sort

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/1873/A) &nbsp;|&nbsp; **Solved:** 2026-08-15

---

## 📝 Summary

Accepted solution for Short Sort on Codeforces.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Direct simulation / brute force**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n) (estimated)` | `~O(1) (estimated)` |

## 🏷️ Tags

`brute force` `implementation`

<details>
<summary>💻 View solution</summary>

```python
t = int(input())
for _ in range(t):
    a = input()
    if a in {'bca','cab'}:
        print('NO')
    else:
        print("YES")
```

</details>
