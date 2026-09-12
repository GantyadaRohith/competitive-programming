# 🟠 best-time-to-buy-and-sell-stock-ii — Best Time to Buy and Sell Stock II

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/) &nbsp;|&nbsp; **Solved:** 2026-03-07

---

## 📝 Summary

Determine the maximum profit from buying and selling stocks multiple times.

## 🔍 Key Observation

The key insight is to accumulate profits by buying at the lowest price and selling at the next higher price.

## ⚙️ Algorithm

1. Initialize two variables, `mi` (minimum price) and `ma` (maximum profit). Set `mi` to infinity and `ma` to 0.
2. Iterate through the list of prices.
3. For each price, update `mi` if the current price is lower than `mi`.
4. If the current price is higher than `mi`, calculate the profit as `price - mi` and add it to `total`.
5. Update `mi` to the current price.
6. Return the total profit.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to a single pass through the list of prices.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`short` `lowercase` `topic` `tags`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mi = float('inf')   
        ma = 0              
        total = 0
        for price in prices:
            if price < mi:
                mi = price
            else: 
                res = price - mi
                mi = price
                total+=res
        return total


```

</details>
