# 🟠 rectangle-area — Rectangle Area

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/rectangle-area/) &nbsp;|&nbsp; **Solved:** 2026-02-24

---

## 📝 Summary

Calculate the area of overlap between two rectangles and return the total area of both rectangles.

## 🔍 Key Observation

Identify the overlap by finding the maximum of the left edges and the minimum of the right edges, and similarly for the top and bottom edges.

## ⚙️ Algorithm

1. Calculate the area of each rectangle using the formula: width * height.
2. Determine the overlap dimensions by finding the maximum of the left edges and the minimum of the right edges, and similarly for the top and bottom edges.
3. If there is an overlap, calculate its area.
4. Return the total area by adding the areas of both rectangles and subtracting the overlap area.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(1) due to constant-time operations.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`rectangle` `area` `overlap`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        rect1 = abs((ax2-ax1)*(ay2-ay1))
        rect2= abs((bx2-bx1)*(by2-by1))
        overlap_h,overlap_w = 0,0
        overlap_area = 0
        if min(ax2,bx2)>max(ax1,bx1):
            overlap_h = min(ax2,bx2)-max(ax1,bx1)  
        if min(ay2,by2) > max(ay1,by1):
            overlap_w = min(ay2,by2)-max(ay1,by1)
        if overlap_h <= 0 or overlap_w <= 0:
            return rect1+rect2
        overlap_area = overlap_h*overlap_w
        return rect1+rect2-overlap_area
```

</details>
