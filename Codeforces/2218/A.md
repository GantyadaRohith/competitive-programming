# 🔵 2218A — The 67th Integer Problem

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/2218/A) &nbsp;|&nbsp; **Solved:** 2026-08-16

---

## 📝 Summary

Given a number of test cases, print each test case's input as an integer.

## 🔍 Key Observation

The problem requires reading an integer for each test case and printing it back.

## ⚙️ Algorithm

The solution involves reading the number of test cases first, then for each test case, reading an integer from the input and printing it.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) where n is the number of test cases, as each test case requires a single read and print operation.` | `O(1) auxiliary space, as the solution uses a constant amount of extra space regardless of the input size.` |

## 🏷️ Tags

`simple` `input` `output` `integer`

<details>
<summary>💻 View solution</summary>

```python
t = int(input())
for _ in range(t):
    print(int(input()))
```

</details>
