# 🔵 116A — Tram

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/116/A) &nbsp;|&nbsp; **Solved:** 2026-07-27

---

## 📝 Summary

Given a sequence of tram operations, determine the maximum number of passengers on the tram at any point.

## 🔍 Key Observation

The key insight is to maintain a running total of passengers on the tram and keep track of the maximum value encountered.

## ⚙️ Algorithm

1. Initialize `total` to 0 and `maxi` to negative infinity.
2. For each tram operation, update `total` by subtracting the number of passengers getting off and adding the number of passengers getting on.
3. Update `maxi` if the current `total` is greater than `maxi`.
4. After processing all operations, `maxi` contains the maximum number of passengers on the tram at any point.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to a single pass through the input.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`implementation` `tram` `operations`

<details>
<summary>💻 View solution</summary>

```python
n = int(input())
total = 0
maxi = -float('inf')
for _ in range(n):
    out,ini = map(int,input().split())
    total = total-out+ini
    maxi = max(maxi,total)
print(maxi)
```

</details>
