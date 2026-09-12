# 🟠 ipo — IPO

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/ipo/) &nbsp;|&nbsp; **Solved:** 2026-02-26

---

## 📝 Summary

Given an array of capital and profit values, determine the maximum capital that can be accumulated by investing in projects up to a given number of times, starting with an initial capital.

## 🔍 Key Observation

Use a min-heap to track available projects and a max-heap to track the most profitable projects.

## ⚙️ Algorithm

1. Initialize two heaps: one for projects with available capital and another for projects with maximum profit.
2. Iterate over the projects, pushing those with available capital into the min-heap.
3. For each investment opportunity, pop the most profitable project from the max-heap and add its profit to the current capital.
4. Repeat steps 2-3 until the number of investments is reached or no more projects with available capital are available.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O((k + n) log n) due to heap operations.` | `O(n) auxiliary space for the heaps.` |

## 🏷️ Tags

`heap` `greedy` `capital` `investment`

<details>
<summary>💻 View solution</summary>

```python
import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        out = []
        Maxpro = []
        for i in range(len(profits)):
            heapq.heappush(out , (capital[i] , profits[i]))
        for _ in range(k):
            while out and out[0][0] <= w:
                heapq.heappush(Maxpro, -heapq.heappop(out)[1])
            if not Maxpro:
                break
            w+= -heapq.heappop(Maxpro)
        return w
```

</details>
