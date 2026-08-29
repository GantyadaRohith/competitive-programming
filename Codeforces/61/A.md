# 🔵 61A — Ultra-Fast Mathematician

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/61/A) &nbsp;|&nbsp; **Solved:** 2026-08-25

---

## 📝 Summary

Given two binary strings of equal length, the problem asks to compute a new binary string where each character is '1' if the corresponding characters in the input strings differ, and '0' if they are the same.

## 🔍 Key Observation

The required operation is equivalent to a bitwise XOR applied character-by-character to the two input strings.

## ⚙️ Algorithm

**Direct character-by-character comparison and string building.**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(N)` | `O(N)` |

## 🏷️ Tags

`implementation` `string` `bitwise`

<details>
<summary>💻 View solution</summary>

```python
n1 = input()
n2 = input()
s = ''
for i in range(len(n1)):
    if n1[i] == n2[i]:
        s+='0'
    else:
        s+='1'
print(s)
```

</details>
