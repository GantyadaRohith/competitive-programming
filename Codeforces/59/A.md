# 🔵 59A — Word

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/59/A) &nbsp;|&nbsp; **Solved:** 2026-07-27

---

## 📝 Summary

Given a string, convert it to all lowercase or all uppercase based on the count of lowercase and uppercase letters.

## 🔍 Key Observation

The key insight is to count the number of lowercase and uppercase letters and then decide the case based on the count.

## ⚙️ Algorithm

1. Read the input string `st`.
2. Initialize counters `lower` and `upper` to zero.
3. Iterate through each character `i` in the string:
   - If `i` is lowercase, increment `lower`.
   - If `i` is uppercase, increment `upper`.
4. Compare `lower` and `upper`:
   - If `lower` is less than `upper`, convert the entire string to uppercase.
   - Otherwise, convert the entire string to lowercase.
5. Print the resulting string.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to the single pass through the string.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`implementation` `strings`

<details>
<summary>💻 View solution</summary>

```python
st = input()
lower = upper = 0
for i in st:
    if i.islower():
        lower+=1
    else:
        upper+=1
if lower < upper:
    print(st.upper())
else:
    print(st.lower())
```

</details>
