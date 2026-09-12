# 🟠 fibonacci-number — Fibonacci Number

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/fibonacci-number/) &nbsp;|&nbsp; **Solved:** 2026-07-09

---

## 📝 Summary

Calculate the nth Fibonacci number using dynamic programming.

## 🔍 Key Observation

Using dynamic programming to store previously computed Fibonacci numbers to avoid redundant calculations.

## ⚙️ Algorithm

1. Initialize an array `dp` of size `n+1` to store Fibonacci numbers. Set `dp[0]` to 0 and `dp[1]` to 1.
2. Iterate from 2 to `n`, filling in each `dp[i]` as the sum of `dp[i-1]` and `dp[i-2]`.
3. Return `dp[n]` as the nth Fibonacci number.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to a single pass through the array of size `n+1`.` | `O(n) auxiliary space used for the `dp` array.` |

## 🏷️ Tags

`dynamic-programming` `fibonacci` `memoization`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        dp = [0]*(n+1)
        dp[1] = 1
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
```

</details>
