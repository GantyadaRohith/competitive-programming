# 🔵 71A — Way Too Long Words

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/71/A) &nbsp;|&nbsp; **Solved:** 2026-07-27

---

## 📝 Summary

Given a list of words, print each word except those with 10 or more characters, replacing words longer than 10 characters with their first and last characters and the length of the middle characters.

## 🔍 Key Observation

Replace words longer than 10 characters with their first and last characters and the length of the middle characters.

## ⚙️ Algorithm

1. Read the number of words `n` from input.
2. For each word `s` in the input:
   - If the length of `s` is less than or equal to 10, print `s`.
   - If the length of `s` is greater than 10, print the first character, the length of the middle characters, and the last character of `s`.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n * m), where n is the number of words and m is the average length of the words.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`strings` `short` `lowercase` `topic`

<details>
<summary>💻 View solution</summary>

```python
n = int(input())
out = []
for i in range(n):
    s = input()
    n = len(s)
    if len(s)<=10:
        print(s)
    else:
        print(s[0]+str(len(s[1:n-1]))+s[-1])

```

</details>
