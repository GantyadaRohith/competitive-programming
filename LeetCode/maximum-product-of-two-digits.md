# 🟠 maximum-product-of-two-digits — Maximum Product of Two Digits

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/maximum-product-of-two-digits/) &nbsp;|&nbsp; **Solved:** 2026-07-25

---

## 📝 Summary

Given a positive integer, find the maximum product of two digits.

## 🔍 Key Observation

The maximum product of two digits can be achieved by selecting the two largest digits.

## ⚙️ Algorithm

1. Convert the integer to a string to easily access each digit.
2. Use a priority queue (min-heap) to efficiently find the two largest digits.
3. Pop the two largest digits from the heap and calculate their product.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log n) due to sorting the digits.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`short` `lowercase` `maximum` `product` `digits`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def maxProduct(self, n: int) -> int:
        pq = []
        for i in str(n):
            heapq.heappush(pq,-(int(i)))
        maxi = -(heapq.heappop(pq))
        mini = -(heapq.heappop(pq))
        return maxi*mini
        
            
```

</details>
