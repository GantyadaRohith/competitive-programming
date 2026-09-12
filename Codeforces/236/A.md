# 🔵 236A — Boy or Girl

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/236/A) &nbsp;|&nbsp; **Solved:** 2026-08-14

---

## 📝 Summary

Given a string of characters, determine if it contains an equal number of 'boy' and 'girl' characters.

## 🔍 Key Observation

The problem can be solved by checking the parity of the set of characters in the string.

## ⚙️ Algorithm

1. Read the input string `a`.
2. Convert the string to a set `s` to remove duplicates.
3. Check if the length of the set `s` is odd.
4. If odd, print 'IGNORE HIM!'.
5. If even, print 'CHAT WITH HER!'.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to the conversion of the string to a set.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`short` `implementation` `strings`

<details>
<summary>💻 View solution</summary>

```python
#wjmzbmr
a = input()
s = set(a)
if len(s)&1:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")
```

</details>
