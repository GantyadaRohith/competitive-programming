# 🟠 minimum-size-subarray-sum — Minimum Size Subarray Sum

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/minimum-size-subarray-sum/) &nbsp;|&nbsp; **Solved:** 2026-02-25

---

## 📝 Summary

Find the minimum length of a contiguous subarray whose sum is at least the target value.

## 🔍 Key Observation

Use a sliding window to efficiently track the sum of subarrays and adjust the window size based on the sum.

## ⚙️ Algorithm

Initialize two pointers, `left` and `right`, to mark the current window. Iterate through the array with `right`, adding elements to the sum. If the sum is greater than or equal to the target, update the minimum length and shrink the window from the left. Continue this process until the end of the array.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to a single pass through the array with two pointers.` | `O(1) auxiliary space used for variables.` |

## 🏷️ Tags

`short` `lowercase` `topic` `tags`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        minlr = float('inf')
        s = 0
        left = 0
        for r in range(n):
            s += nums[r]
            while(s>=target):
                minlr = min(minlr,r - left + 1)
                s-=nums[left]
                left+=1
        if minlr == float('inf'):
            return 0
        else:
            return minlr

```

</details>
