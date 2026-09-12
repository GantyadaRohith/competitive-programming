# 🟠 k-closest-points-to-origin — K Closest Points to Origin

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/k-closest-points-to-origin/) &nbsp;|&nbsp; **Solved:** 2026-02-24

---

## 📝 Summary

Find the k closest points to the origin in a list of points.

## 🔍 Key Observation

Use a min-heap to efficiently find the k closest points based on their distance from the origin.

## ⚙️ Algorithm

1. Initialize an empty list `out` to store tuples of (distance, index, point) and an empty list `res` to store the result.
2. Iterate over each point, calculate its distance from the origin using the Euclidean distance formula, and push the tuple into the heap.
3. Pop the smallest distance from the heap `k` times and append the corresponding point to the result list `res`.
4. Return the result list `res`.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log n) due to the heap operations.` | `O(n) auxiliary space for the heap and result list.` |

## 🏷️ Tags

`heap` `distance` `k-closest`

<details>
<summary>💻 View solution</summary>

```python
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        out = []
        res = []
        for i in range(len(points)):
            x1,y1 = points[i]
            dist = math.sqrt(x1**2+y1**2)
            heapq.heappush(out , (dist , i , [x1,y1]))
        for i in range(k):
            res.append(heapq.heappop(out)[2])
        return res
```

</details>
