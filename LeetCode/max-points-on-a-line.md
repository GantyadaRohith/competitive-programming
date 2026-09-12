# 🟠 max-points-on-a-line — Max Points on a Line

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/max-points-on-a-line/) &nbsp;|&nbsp; **Solved:** 2026-02-24

---

## 📝 Summary

Given a list of points on a 2D plane, find the maximum number of points that lie on the same straight line.

## 🔍 Key Observation

The key insight is to use the slope of lines formed by pairs of points to determine if they are collinear.

## ⚙️ Algorithm

1. For each pair of points, calculate the slope of the line connecting them. 2. Use a dictionary to count the number of points that have the same slope with the current pair. 3. Update the result with the maximum count found.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n^3) due to the triple nested loop.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`medium` `math` `geometry`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 2:
            return 2
        elif len(points) == 1:
            return 1
        else:
            result = 1
            for i in range(len(points)):
                x1,y1 = points[i]
                for j in range(i+1,len(points)):
                    x2,y2 = points[j]
                    cnt = 2
                    for k in range(j+1,len(points)):
                        x3,y3 = points[k]
                        if (y2-y1)*(x3-x1) == (y3-y1)*(x2-x1):
                            cnt+=1
                    result = max(cnt,result)
            return result
```

</details>
