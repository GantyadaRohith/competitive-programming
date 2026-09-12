# 🔵 281A — Word Capitalization

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/281/A) &nbsp;|&nbsp; **Solved:** 2026-08-20

---

## 📝 Summary

Given a word, capitalize the first letter if it is lowercase.

## 🔍 Key Observation

The first character of the word determines whether it needs to be capitalized.

## ⚙️ Algorithm

1. Read the input word.
2. Check if the first character is lowercase.
3. If so, capitalize it and print the modified word.
4. If not, print the original word.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(1) due to constant-time operations.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`short` `lowercase` `string` `capitalization`

<details>
<summary>💻 View solution</summary>

```python
word = input()
if word[0].islower():
    print(word[0].upper()+word[1:])
else:
    print(word)
```

</details>
