# 🔵 1669A — Division?

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/1669/A) &nbsp;|&nbsp; **Solved:** 2026-08-25

---

## 📝 Summary

The problem asks to determine a participant's competitive programming division (Division 1, 2, 3, or 4) based on their given rating, using a set of predefined rating thresholds.

## 🔍 Key Observation

The problem requires a direct implementation of the given rating-to-division mapping rules using conditional statements, as the thresholds are fixed and simple.

## ⚙️ Algorithm

**Direct implementation with conditional statements (if-elif-else).**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(t)` | `O(1)` |

## 🏷️ Tags

`implementation` `conditionals` `basics`

<details>
<summary>💻 View solution</summary>

```python
t = int(input())
for _ in range(t):
    rat = input()
    if rat[0]!='-':
        rat = int(rat)
    else:
        rat = -1*int(rat[1:])
    if rat<=1399:
        print("Division 4")
    elif rat<=1599:
        print("Division 3")
    elif rat<=1899:
        print("Division 2")
    else:
        print("Division 1")
```

</details>
