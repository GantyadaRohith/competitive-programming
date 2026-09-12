# 🟠 container-with-most-water — Container With Most Water

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/container-with-most-water/) &nbsp;|&nbsp; **Solved:** 2026-07-06

---

## 📝 Summary

Given an array of non-negative integers representing the heights of vertical lines, find the maximum area of water that can be contained between any two lines.

## 🔍 Key Observation

The maximum area is determined by the shorter line and the distance between them.

## ⚙️ Algorithm

1. Initialize two pointers, `l` at the start and `r` at the end of the array.
2. Calculate the area using the shorter line and the distance between the pointers.
3. Update the maximum area if the current area is greater.
4. Move the pointer pointing to the shorter line inward.
5. Repeat steps 2-4 until the pointers meet.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to the single pass through the array.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`two-pointer` `array` `water`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r = 0,len(height) - 1
        maxi = 0
        while(l<r):
            area = (r-l) *min(height[l],height[r])
            maxi = max(maxi,area)
            if height[l]>=height[r]:
                r-=1
            else:
                l+=1
        return maxi
```

</details>
