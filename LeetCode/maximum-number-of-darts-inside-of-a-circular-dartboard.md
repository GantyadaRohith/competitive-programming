# 🟠 maximum-number-of-darts-inside-of-a-circular-dartboard — Maximum Number of Darts Inside of a Circular Dartboard

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/maximum-number-of-darts-inside-of-a-circular-dartboard/) &nbsp;|&nbsp; **Solved:** 2026-02-24

---

## 📝 Summary

Given a circular dartboard and a set of darts, find the maximum number of darts that can be inside the dartboard.

## 🔍 Key Observation

The key insight is to consider each dart as a center and count the number of darts within a circle of radius `r` centered at that dart.

## ⚙️ Algorithm

1. Iterate over each dart in the list.
2. For each dart, consider it as the center of a circle with radius `r`.
3. For each dart, calculate the distance from it to every other dart.
4. Count how many other darts are within the circle of radius `r` centered at the current dart.
5. Keep track of the maximum number of darts found in any circle.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n^3) due to the nested loops and distance calculations.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`short` `lowercase` `topic` `tags`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def numPoints(self, darts: List[List[int]], r: int) -> int:
        cnt = 0
        for i in range(len(darts)):
            x1,y1 = darts[i]
            for j in range(360):
                h,k = x1-r*math.sin(j),y1-r*math.cos(j)
                maxDarts = 0
                for l in range(len(darts)):
                    x2,y2 = darts[l]
                    dist = math.sqrt((x2-h)**2 + (y2-k)**2) 
                    if (dist-r) <= 0.001:
                        maxDarts+=1
                cnt = max(cnt,maxDarts)
        return cnt
```

</details>
