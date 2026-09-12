# 🟠 minimize-manhattan-distances — Minimize Manhattan Distances

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/minimize-manhattan-distances/) &nbsp;|&nbsp; **Solved:** 2026-02-24

---

## 📝 Summary

Given a list of points in a 2D plane, find the minimum Manhattan distance between any two points.

## 🔍 Key Observation

The Manhattan distance between two points (x1, y1) and (x2, y2) is |x1 - x2| + |y1 - y2|. The key insight is to sort the points based on their Manhattan distances to the origin and then find the minimum distance between consecutive points.

## ⚙️ Algorithm

1. Calculate the Manhattan distance of each point from the origin (0, 0) and store these distances in two separate lists, `u` and `v`, where `u[i] = x[i] + y[i]` and `v[i] = x[i] - y[i]`. 2. Sort the lists `u` and `v`. 3. Find the maximum and minimum values in `u` and `v`. 4. For each point, calculate the maximum and minimum distances from the origin to the point using the sorted lists. 5. Find the minimum distance between consecutive points in the sorted list of points.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log n) due to sorting.` | `O(n) auxiliary space.` |

## 🏷️ Tags

`short` `lowercase` `algorithm` `sorting`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def minimumDistance(self, points: List[List[int]]) -> int:
        n = len(points)
        u = []
        v = []
        for x, y in points:
            u.append(x + y)
            v.append(x - y)
        max_u = max(u)
        min_u = min(u)
        max_v = max(v)
        min_v = min(v)
        second_max_u = sorted(u)[-2]
        second_min_u = sorted(u)[1]
        second_max_v = sorted(v)[-2]
        second_min_v = sorted(v)[1]
        ans = float('inf')
        for i in range(n):
            curr_max_u = second_max_u if u[i] == max_u else max_u
            curr_min_u = second_min_u if u[i] == min_u else min_u
            curr_max_v = second_max_v if v[i] == max_v else max_v
            curr_min_v = second_min_v if v[i] == min_v else min_v
            dist = max(curr_max_u - curr_min_u,
                       curr_max_v - curr_min_v)
            ans = min(ans, dist)
        return ans
```

</details>
