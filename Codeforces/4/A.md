# 🔵 4A — Watermelon

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/4/A) &nbsp;|&nbsp; **Solved:** 2026-07-25

---

## 📝 Summary

Given a positive integer representing the weight of a watermelon, determine if it can be split into two even parts.

## 🔍 Key Observation

The key insight is that a watermelon can be split into two even parts if and only if its weight is even and greater than 2.

## ⚙️ Algorithm

1. Check if the weight is even and greater than 2. If not, print 'NO'.
2. Iterate through possible values of the first part of the split (from 1 to weight-1).
3. For each value, check if the second part (weight - value) is also even.
4. If such a pair is found, print 'YES'. If no such pair exists, print 'NO'.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to the loop through possible values of the first part.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`short` `lowercase` `watermelon` `split`

<details>
<summary>💻 View solution</summary>

```python
weight = int(input())
if (weight%2) != 0 or weight<=2:
    print("NO")
else:
    flag = 0
    for i in range(1,weight):
        if i%2 == 0 and (weight-i)%2 == 0:
            flag = 1
            break

    if flag:
        print("YES")
    else:
        print("NO")

```

</details>
