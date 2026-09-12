# 🟠 coin-change — Coin Change

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/coin-change/) &nbsp;|&nbsp; **Solved:** 2026-07-09

---

## 📝 Summary

Given a list of coin denominations and an amount, find the minimum number of coins required to make up that amount. Return -1 if it's not possible.

## 🔍 Key Observation

Dynamic programming is used to build up solutions for subproblems, ensuring that each coin is considered only once for each amount.

## ⚙️ Algorithm

1. Initialize a DP array `dp` where `dp[i]` represents the minimum number of coins needed to make up amount `i`. Set `dp[0]` to 0 since 0 coins are needed to make up 0 amount.
2. Iterate over each coin in the `coins` list.
3. For each coin, update the `dp` array by considering all possible amounts up to the current coin's value. Update `dp[x]` to be the minimum of its current value and `dp[x - coin] + 1` (using the coin).
4. After processing all coins, `dp[amount]` will contain the minimum number of coins needed to make up the given amount. If it's still `float('inf')`, return -1 indicating it's not possible.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n * amount), where n is the number of coins.` | `O(amount) for the DP array.` |

## 🏷️ Tags

`dp` `coin change` `greedy`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1

```

</details>
