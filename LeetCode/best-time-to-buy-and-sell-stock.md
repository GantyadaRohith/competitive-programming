# 🟠 best-time-to-buy-and-sell-stock — Best Time to Buy and Sell Stock

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) &nbsp;|&nbsp; **Solved:** 2026-07-08

---

## 📝 Summary

Find the maximum profit from buying and selling a stock once.

## 🔍 Key Observation

The key insight is to keep track of the minimum price encountered so far and calculate the potential profit at each price, updating the maximum profit accordingly.

## ⚙️ Algorithm

1. Initialize `mi` to infinity and `ma` to 0.
2. Iterate through each price in the `prices` list.
3. If the current price is less than `mi`, update `mi` to the current price.
4. Otherwise, calculate the potential profit as `price - mi` and update `ma` if this profit is greater than the current `ma`.
5. Return `ma` as the maximum profit.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to a single pass through the prices list.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`short` `lowercase` `topic` `tags`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mi = float('inf')   # minimum price so far
        ma = 0              # maximum profit so far

        for price in prices:
            if price < mi:
                mi = price
            else:
                ma = max(ma, price - mi)

        return ma



```

</details>
