# 🟠 minimum-lines-to-represent-a-line-chart — Minimum Lines to Represent a Line Chart

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/minimum-lines-to-represent-a-line-chart/) &nbsp;|&nbsp; **Solved:** 2026-02-24

---

## 📝 Summary

Given a list of stock prices, determine the minimum number of lines required to represent the line chart.

## 🔍 Key Observation

The key insight is to use the slope of consecutive lines to determine if they are the same.

## ⚙️ Algorithm

1. Sort the stock prices to ensure they are in chronological order.
2. Initialize the count of lines to 1 (since the first line is always valid).
3. Calculate the slope of the first two lines.
4. Iterate through the stock prices starting from the third one.
5. For each pair of consecutive lines, calculate their slopes.
6. If the slopes are different, increment the line count and update the previous slopes.
7. Return the total line count.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log n) due to sorting.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`short` `lowercase` `topic` `tags`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        cnt = 1
        stockPrices.sort()
        if len(stockPrices)<=1:
            return 0
        x1,y1 = stockPrices[0]
        x2,y2 = stockPrices[1]
        prev_dy = (y2-y1)
        prev_dx = (x2-x1)
        for i in range(1,len(stockPrices)-1):
            x1,y1 = stockPrices[i]
            x2,y2 = stockPrices[i+1]
            dy,dx = (y2-y1),(x2-x1)
            if prev_dy*dx!=prev_dx*dy:
                cnt+=1
                prev_dx,prev_dy = dx,dy
        return cnt
            
```

</details>
