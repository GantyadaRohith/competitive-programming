# 🟠 find-peak-element — Find Peak Element

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/find-peak-element/) &nbsp;|&nbsp; **Solved:** 2026-07-01

---

## 📝 Summary

Find the index of the peak element in a list of integers.

## 🔍 Key Observation

The peak element is greater than its neighbors.

## ⚙️ Algorithm

Use binary search to find the peak element. Compare the middle element with its next element. If the middle element is greater, the peak is in the left half; otherwise, it's in the right half. Continue this process until the low index meets the right index.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(log n) due to binary search.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`binary search` `peak element`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low,right = 0,len(nums)-1
        while low<right:
            mid = (low+right)//2
            if nums[mid] > nums[mid+1]:
                right = mid
            else:
                low = mid+1
        return low
```

</details>
