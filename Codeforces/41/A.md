# 🔵 41A — Translation

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/41/A) &nbsp;|&nbsp; **Solved:** 2026-08-20

---

## 📝 Summary

Given two strings, determine if one is the reverse of the other.

## 🔍 Key Observation

The key insight is to check if the first string is the reverse of the second string.

## ⚙️ Algorithm

The algorithm involves reversing the second string and comparing it to the first string. If they are the same, the first string is the reverse of the second string.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to the reversal operation.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`string` `reverse` `check`

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
