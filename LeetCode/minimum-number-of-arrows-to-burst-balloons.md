# 🟠 minimum-number-of-arrows-to-burst-balloons — Minimum Number of Arrows to Burst Balloons

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/) &nbsp;|&nbsp; **Solved:** 2026-02-26

---

## 📝 Summary

Determine the minimum number of arrows needed to burst all balloons.

## 🔍 Key Observation

Sort balloons by their end points to minimize overlap.

## ⚙️ Algorithm

1. Sort balloons by their end points. This ensures that the last arrow can burst the most balloons first.
2. Initialize an arrow count and set the end point of the first balloon.
3. Iterate through the sorted balloons, incrementing the arrow count when the current balloon's start point is greater than the current arrow's end point.
4. Update the end point to the current balloon's end point.
5. Return the total number of arrows used.

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
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        points.sort(key=lambda x: x[1]) 
        arrows = 1
        end = points[0][1]

        for s, e in points:
            if s > end:          
                arrows += 1
                end = e          

        return arrows
```

</details>
