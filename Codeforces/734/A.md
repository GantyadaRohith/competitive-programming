# 🔵 734A — Anton and Danik

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/734/A) &nbsp;|&nbsp; **Solved:** 2026-08-20

---

## 📝 Summary

Accepted solution for Anton and Danik on Codeforces.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Direct simulation / brute force**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `~O(n) (estimated)` | `~O(1) (estimated)` |

## 🏷️ Tags

`implementation` `strings`

<details>
<summary>💻 View solution</summary>

```python
n = int(input())
st = input()
a = b = 0
for i in st:
    if i == 'A':
        a+=1
    else:
        b+=1
if a == b:
    print("Friendship")
elif a>b:
    print("Anton")
else:
    print("Danik")
```

</details>
