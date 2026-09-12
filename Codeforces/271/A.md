# 🔵 271A — Beautiful Year

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/271/A) &nbsp;|&nbsp; **Solved:** 2026-08-20

---

## 📝 Summary

Find the first year after the given year that has exactly four distinct digits.

## 🔍 Key Observation

The key insight is to check each subsequent year for exactly four distinct digits.

## ⚙️ Algorithm

1. Start from the given year and incrementally check each year.
2. For each year, convert it to a string and use a set to track unique digits.
3. If the set size is four, print the year and break the loop.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log n) due to sorting.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`short` `lowercase` `problem-solving` `algorithm`

<details>
<summary>💻 View solution</summary>

```python
import sys
input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp():
    return(int(input()))

year = inp()
for i in range(year+1,9013):
    s = set()
    n = 0
    for j in str(i):
        if j not in s:
            s.add(j)
            n+=1
        else:
            break
    if n == 4:
        print(i)
        break
```

</details>
