# 🟠 height-checker — Height Checker

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/height-checker/) &nbsp;|&nbsp; **Solved:** 2025-12-03

---

## 📝 Summary

Given an array of integers representing the heights of students, count how many students are not in their correct positions.

## 🔍 Key Observation

The key insight is to compare the sorted array with the original array to count mismatches.

## ⚙️ Algorithm

1. Sort the array of heights.
2. Initialize a counter to zero.
3. Iterate through the sorted array and compare each element with the corresponding element in the original array.
4. If they are not equal, increment the counter.
5. Return the counter as the result.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log n) due to sorting.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`short` `lowercase` `sort` `count`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        x = sorted(heights)
        j = 0
        for i in range(len(x)):
            if heights[i] != x[i]:
                j+=1
        return j
```

</details>
