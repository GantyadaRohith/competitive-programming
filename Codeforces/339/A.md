# 🔵 339A — Helpful Maths

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/339/A) &nbsp;|&nbsp; **Solved:** 2026-08-14

---

## 📝 Summary

Given a string of numbers separated by '+', sort them in ascending order.

## 🔍 Key Observation

The key insight is to split the string by '+' and then sort the resulting list of numbers.

## ⚙️ Algorithm

1. Read the input string.
2. Split the string by '+' to get a list of numbers.
3. Sort the list of numbers.
4. Join the sorted list back into a string with '+' as the separator.
5. Print the resulting string.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log n) due to sorting.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`short` `implementation` `sortings` `strings`

<details>
<summary>💻 View solution</summary>

```python
st = input()

nums = st.split('+')
nums.sort()

print('+'.join(nums))
```

</details>
