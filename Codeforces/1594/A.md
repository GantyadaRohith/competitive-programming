# 🔵 1594A — Consecutive Sum Riddle

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/1594/A) &nbsp;|&nbsp; **Solved:** 2026-08-14

---

## 📝 Summary

Given a positive integer n, find two consecutive integers that sum to n.

## 🔍 Key Observation

The key insight is that the two consecutive integers are n/2 and n/2 + 1.

## ⚙️ Algorithm

1. Read the number of test cases T.
2. For each test case:
   a. Read the integer n.
   b. Calculate the two consecutive integers as n/2 and n/2 + 1.
   c. Print the result.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(1) due to constant-time operations.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`math` `simple`

<details>
<summary>💻 View solution</summary>

```python
T = int(input())
for i in range(T):
    n = int(input())
    print(1-n,n)

```

</details>
