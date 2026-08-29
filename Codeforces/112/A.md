# 🔵 112A — Petya and Strings

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/112/A) &nbsp;|&nbsp; **Solved:** 2026-08-20

---

## 📝 Summary

Accepted solution for Petya and Strings on Codeforces.

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
str1 = input()
str2 = input()
a = {}
j = 0
for i in 'abcdefghijklmnopqrstuvwxyz':
    a[i] = j
    j+=1
str1 = str1.lower()
str2 = str2.lower()
if str1 == str2:
    print(0)
else:
    for i in range(len(str1)):
        if a[str1[i]] > a[str2[i]]:
            print(1)
            break
        elif a[str1[i]] < a[str2[i]]:
            print(-1)
            break

```

</details>
