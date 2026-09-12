# 🔵 1669A — Division?

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/1669/A) &nbsp;|&nbsp; **Solved:** 2026-08-25

---

## 📝 Summary

Given a rating, determine the division level based on a specific rating range.

## 🔍 Key Observation

The solution uses a series of conditional checks to determine the division level based on the input rating.

## ⚙️ Algorithm

The code reads the input rating, converts it to an integer, and then checks against predefined ranges to determine the division level. It handles negative ratings by converting them to positive.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(1) due to constant-time operations.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`easy` `lowercase` `rating` `division`

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
