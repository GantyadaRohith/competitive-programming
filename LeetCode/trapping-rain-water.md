# 🟠 trapping-rain-water — Trapping Rain Water

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/trapping-rain-water/) &nbsp;|&nbsp; **Solved:** 2025-12-10

---

## 📝 Summary

Given an array of non-negative integers representing the elevation of walls, calculate the total amount of water that can be trapped between the walls.

## 🔍 Key Observation

The solution uses a two-pointer technique to find the maximum height of walls on both sides of the current position and calculates the trapped water based on the minimum of these heights.

## ⚙️ Algorithm

1. Initialize two pointers, `l` at the start and `r` at the end of the array, and two variables, `lm` and `rm`, to keep track of the maximum height of walls seen from the left and right, respectively.
2. While `l` is less than `r`:
   - If the height at `l` is less than the height at `r`:
     - If `height[l]` is greater than or equal to `lm`, update `lm` to `height[l]`.
     - Otherwise, add the difference between `lm` and `height[l]` to `trap` and increment `l`.
   - Else:
     - If `height[r]` is greater than or equal to `rm`, update `rm` to `height[r]`.
     - Otherwise, add the difference between `rm` and `height[r]` to `trap` and decrement `r`.
3. Return the total trapped water.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to a single pass through the array.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`short` `lowercase` `trapping` `rain` `water`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        lm = rm = 0
        trap = 0

        while l < r:
            if height[l] < height[r]:
                if height[l] >= lm:
                    lm = height[l]
                else:
                    trap += lm - height[l]
                l += 1
            else:
                if height[r] >= rm:
                    rm = height[r]
                else:
                    trap += rm - height[r]
                r -= 1

        return trap
```

</details>
