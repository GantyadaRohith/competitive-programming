# 🟠 minimum-total-price-after-applying-discounts — Minimum Total Price After Applying Discounts

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/minimum-total-price-after-applying-discounts/) &nbsp;|&nbsp; **Solved:** 2026-08-09

---

## 📝 Summary

Given a list of prices and discounts, calculate the minimum total price after applying discounts in ascending order.

## 🔍 Key Observation

Sort both prices and discounts in descending order to apply discounts in the most effective way.

## ⚙️ Algorithm

1. Sort both the prices and discounts in descending order.
2. Initialize a variable `cost` to accumulate the total price.
3. Iterate through the sorted discounts and prices:
   - Apply the discount to the current price and add to `cost`.
4. If there are remaining prices after applying discounts, add their sum to `cost`.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log n) due to sorting.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`sort` `discount` `price`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        discounts.sort(reverse = True)
        prices.sort(reverse = True)
        cost = 0.00
        for i in range(len(discounts)):
            if i == len(prices):
                break
            cost+=(prices[i] * (100 - discounts[i])) / 100
        print(cost)
        if len(discounts)<len(prices):
            cost+=sum(prices[len(discounts):])
            print(cost)
        return cost
        
```

</details>
