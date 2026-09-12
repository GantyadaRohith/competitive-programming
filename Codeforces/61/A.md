# 🔵 61A — Ultra-Fast Mathematician

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/61/A) &nbsp;|&nbsp; **Solved:** 2026-08-25

---

## 📝 Summary

Given two numbers, determine the bitwise XOR of their digits.

## 🔍 Key Observation

The XOR operation is used to compare corresponding digits of the two numbers.

## ⚙️ Algorithm

The code iterates over the digits of the two numbers simultaneously. For each pair of digits, it checks if they are equal. If they are, it appends '0' to the result string; otherwise, it appends '1'.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to the single pass through the digits of the numbers.` | `O(n) for the result string.` |

## 🏷️ Tags

`bitwise` `xor` `digits`

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
