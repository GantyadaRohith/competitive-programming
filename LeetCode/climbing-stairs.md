# 🟠 climbing-stairs — Climbing Stairs

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/climbing-stairs/) &nbsp;|&nbsp; **Solved:** 2026-07-08

---

## 📝 Summary

Given a staircase with n steps, find the number of distinct ways to climb to the top, where you can take either 1 or 2 steps at a time.

## 🔍 Key Observation

The problem can be solved using dynamic programming to avoid redundant calculations.

## ⚙️ Algorithm

1. Initialize a list `dp` of size `n+1` with all elements set to 0. This list will store the number of ways to reach each step.
2. Set `dp[1]` to 1 and `dp[2]` to 2, as there is only one way to reach the first step and two ways to reach the second step.
3. For each step from 3 to n, calculate the number of ways to reach that step by summing the number of ways to reach the previous two steps (`dp[i-1]` and `dp[i-2]`).
4. Return `dp[n]`, which represents the number of ways to reach the top of the staircase.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to a single pass through the list of size n.` | `O(n) auxiliary space used for the `dp` list.` |

## 🏷️ Tags

`dynamic programming` `fibonacci` `staircase`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        dp = [0]*(n+1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3,n+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[-1]
        
```

</details>
