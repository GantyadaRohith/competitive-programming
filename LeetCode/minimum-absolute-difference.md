# 🟠 minimum-absolute-difference — Minimum Absolute Difference

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/minimum-absolute-difference/) &nbsp;|&nbsp; **Solved:** 2025-11-20

---

## 📝 Summary

Find the pair of numbers in the array with the smallest absolute difference.

## 🔍 Key Observation

Sorting the array allows for efficient comparison of adjacent elements to find the minimum difference.

## ⚙️ Algorithm

1. Sort the array to bring the smallest differences next to each other.
2. Iterate through the sorted array and calculate the difference between each pair of adjacent elements.
3. Track the minimum difference found.
4. Collect all pairs with the minimum difference.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log n) due to sorting.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`short` `lowercase` `sort` `difference`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        out = []
        min_diff = float('inf')
        for i in range(0,len(arr)-1,1):
            diff = arr[i+1] - arr[i]
            min_diff = min(diff,min_diff)
        for i in range(0,len(arr)-1,1):
            if arr[i+1] - arr[i] == min_diff:
                out.append([arr[i],arr[i+1]])
        return out
```

</details>
