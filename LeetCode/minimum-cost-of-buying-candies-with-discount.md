# 🟠 minimum-cost-of-buying-candies-with-discount — Minimum Cost of Buying Candies With Discount

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/) &nbsp;|&nbsp; **Solved:** 2025-11-20

---

## 📝 Summary

Given a list of candy prices, find the minimum cost to buy all candies with a discount on every third candy.

## 🔍 Key Observation

Sort the candies in descending order and buy every third candy at full price, skipping the next two.

## ⚙️ Algorithm

1. Sort the list of candy prices in descending order.
2. Initialize a total cost variable to 0.
3. Iterate through the sorted list, adding every third candy to the total cost.
4. Skip the next two candies after each purchase.
5. Return the total cost.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log n) due to sorting.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`sort` `greedy` `discount`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        total = 0
        i = 0
        while i < len(cost):
            total += cost[i]
            if i + 1 < len(cost):
                total += cost[i+1]
            i += 3  
        return total

```

</details>
