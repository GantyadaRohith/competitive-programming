# 🟠 kth-largest-element-in-an-array — Kth Largest Element in an Array

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/kth-largest-element-in-an-array/) &nbsp;|&nbsp; **Solved:** 2026-07-06

---

## 📝 Summary

Find the k-th largest element in an array.

## 🔍 Key Observation

Use a min-heap to efficiently track the k largest elements.

## ⚙️ Algorithm

1. Initialize an empty min-heap.
2. Iterate through each number in the array, pushing its negative value onto the heap (to simulate a max-heap).
3. If the heap size exceeds k, pop the smallest element (which is the largest in the negative space).
4. After processing all numbers, the top of the heap contains the k-th largest element.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log k) due to heap operations.` | `O(k) auxiliary space for the heap.` |

## 🏷️ Tags

`heap` `priority-queue` `kth-largest`

<details>
<summary>💻 View solution</summary>

```python
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []
        for i in nums:
            heapq.heappush(pq,-i)
        for i in range(k-1):
            heapq.heappop(pq)
        return -1*heapq.heappop(pq)
```

</details>
