# 🔵 41A — Translation

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/41/A) &nbsp;|&nbsp; **Solved:** 2026-08-20

---

## 📝 Summary

Accepted solution for Translation on Codeforces.

## 🔍 Key Observation

Auto-generated from source-code heuristics (no GEMINI_API_KEY configured) -- set one in .env for LLM-authored insight, or edit this section manually.

## ⚙️ Algorithm

**Direct simulation / brute force**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(1)–O(n) (estimated -- could not confidently infer)` | `~O(1) (estimated)` |

## 🏷️ Tags

`implementation` `strings`

<details>
<summary>💻 View solution</summary>

```python
str1 = input()
str2 = input()
if str1 == str2[::-1]:
    print('YES')
else:
    print('NO')
```

</details>
