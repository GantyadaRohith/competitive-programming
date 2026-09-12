# 🟠 maximum-subarray — Maximum Subarray

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/maximum-subarray/) &nbsp;|&nbsp; **Solved:** 2026-07-08

---

## 📝 Summary

Find the contiguous subarray with the largest sum in an array of integers.

## 🔍 Key Observation

The key insight is to use Kadane's Algorithm, which maintains a running sum of the subarray and updates the maximum sum found so far.

## ⚙️ Algorithm

Initialize `curr_sum` and `max_sum` with the first element of the array. Iterate through the array starting from the second element, updating `curr_sum` to be the maximum of the current element or the sum of `curr_sum` and the current element. Update `max_sum` to be the maximum of itself and `curr_sum`. After iterating through the array, `max_sum` contains the maximum subarray sum.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to a single pass through the array.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`kadane` `subarray` `maximum`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = nums[0]
        max_sum = nums[0]
        for i in nums[1:]:
            curr_sum = max(i,curr_sum+i)
            max_sum = max(max_sum,curr_sum)
        return max_sum
```

</details>
