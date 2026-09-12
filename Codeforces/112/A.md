# 🔵 112A — Petya and Strings

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/112/A) &nbsp;|&nbsp; **Solved:** 2026-08-20

---

## 📝 Summary

Given two strings, determine if they are anagrams of each other and return the lexicographical order if they are not.

## 🔍 Key Observation

The key insight is to use a dictionary to map each letter to its position in the alphabet and then compare the positions of corresponding letters in the two strings.

## ⚙️ Algorithm

1. Create a dictionary `a` that maps each letter from 'a' to 'z' to its corresponding position in the alphabet (0 to 25).
2. Convert both input strings to lowercase to ensure case-insensitivity.
3. If the strings are identical, print 0.
4. Otherwise, iterate through the characters of the strings simultaneously.
5. Compare the positions of corresponding characters in the dictionary.
6. If a character in `str1` has a higher position than the corresponding character in `str2`, print 1 and break.
7. If a character in `str1` has a lower position than the corresponding character in `str2`, print -1 and break.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) where n is the length of the strings, as each character is processed once.` | `O(1) auxiliary space, as the dictionary `a` has a fixed size of 26.` |

## 🏷️ Tags

`string` `comparison` `alphabet` `dictionary`

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
