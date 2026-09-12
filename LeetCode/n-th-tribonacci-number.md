# 🟠 n-th-tribonacci-number — N-th Tribonacci Number

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/n-th-tribonacci-number/) &nbsp;|&nbsp; **Solved:** 2026-05-14

---

## 📝 Summary

Calculate the N-th number in the Tribonacci sequence, where each number is the sum of the three preceding ones.

## 🔍 Key Observation

Use dynamic programming to store intermediate results and avoid redundant calculations.

## ⚙️ Algorithm

Initialize an array `dp` of size `n+1` to store the Tribonacci numbers. Set the base cases for `dp[0]`, `dp[1]`, and `dp[2]` to 0, 1, and 1 respectively. Iterate from 3 to `n`, updating each `dp[i]` as the sum of the previous three numbers. Return `dp[n]` as the result.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to a single pass through the array.` | `O(n) auxiliary space for the `dp` array.` |

## 🏷️ Tags

`dynamic programming` `tribonacci` `sequence`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def tribonacci(self, n: int) -> int:
        if n<=2:
            return 1 if n>0 else 0
        dp = [0]*(n+1)
        dp[0] = 0
        dp[1] =  dp[2] = 1
        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2]+dp[i-3]
        return dp[-1]
```

</details>
