# 🔵 486A — Calculating Function

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/486/A) &nbsp;|&nbsp; **Solved:** 2026-07-27

---

## 📝 Summary

Given a positive integer, calculate the difference between the sum of even numbers and the sum of odd numbers up to that integer.

## 🔍 Key Observation

The key insight is to use the formula for the sum of the first n natural numbers and apply it to even and odd numbers separately.

## ⚙️ Algorithm

1. Calculate the number of even numbers up to the given integer `f` using `eve = f//2`.
2. Calculate the number of odd numbers up to the given integer `f` using `odd = f-eve`.
3. Use the formula for the sum of the first n natural numbers to calculate the sum of even numbers: `eve*(eve+1)`. Similarly, calculate the sum of odd numbers: `odd*odd`.
4. Subtract the sum of odd numbers from the sum of even numbers to get the result.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(1) due to constant-time arithmetic operations.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`implementation` `math`

<details>
<summary>💻 View solution</summary>

```python
f = int(input())
eve = f//2
odd = f-eve

total = (eve*(eve+1))-(odd*odd)
print(total)
```

</details>
