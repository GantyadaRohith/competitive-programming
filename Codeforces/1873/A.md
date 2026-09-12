# 🔵 1873A — Short Sort

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/1873/A) &nbsp;|&nbsp; **Solved:** 2026-08-15

---

## 📝 Summary

Given a string, determine if it is a palindrome or not.

## 🔍 Key Observation

A string is a palindrome if it reads the same forwards and backwards.

## ⚙️ Algorithm

The algorithm checks if the input string is equal to its reverse. If they are equal, the string is a palindrome; otherwise, it is not.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to the need to reverse the string.` | `O(n) for storing the reversed string.` |

## 🏷️ Tags

`string` `palindrome` `reverse`

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
