# 🔵 112A — Petya and Strings

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/112/A) &nbsp;|&nbsp; **Solved:** 2026-08-20

---

## 📝 Summary

Given two strings, determine their lexicographical order.

## 🔍 Key Observation

The solution uses a dictionary to map each letter to a unique integer, allowing for a straightforward comparison.

## ⚙️ Algorithm

1. Create a dictionary to map each letter of the alphabet to a unique integer (a=0, b=1, ..., z=25).
2. Convert both input strings to lowercase to ensure case-insensitive comparison.
3. Compare the corresponding characters of both strings using the dictionary values.
4. Return the result based on the comparison: 0 if the strings are equal, 1 if the first string is lexicographically greater, and -1 if the first string is lexicographically smaller.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to the single pass through the strings.` | `O(1) auxiliary space, as the dictionary size is constant.` |

## 🏷️ Tags

`short` `lowercase` `string` `comparison`

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
