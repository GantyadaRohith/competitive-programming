# 🔵 977A — Wrong Subtraction

![Platform](https://img.shields.io/badge/Platform-Codeforces-1F8ACB?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on Codeforces](https://codeforces.com/problemset/problem/977/A) &nbsp;|&nbsp; **Solved:** 2026-07-27

---

## 📝 Summary

Given a number n and an integer k, repeatedly subtract 1 from n if it is not divisible by 10, otherwise divide n by 10, until k operations are performed.

## 🔍 Key Observation

The key insight is to repeatedly perform the operation of subtracting 1 if n is not divisible by 10, otherwise dividing n by 10, until the desired number of operations is performed.

## ⚙️ Algorithm

1. Read the input values of n and k.
2. For k operations:
   a. If n is not divisible by 10, subtract 1 from n.
   b. Otherwise, divide n by 10.
3. Print the final value of n after k operations.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(k) due to the loop that performs k operations.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`implementation` `short`

<details>
<summary>💻 View solution</summary>

```python
n,k = map(int,input().split())
for i in range(k):
    if n%10 != 0:
        n-=1
    else:
        n/=10
print(int(n))
```

</details>
