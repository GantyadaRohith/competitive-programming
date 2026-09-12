# 🟠 running-sum-of-1d-array — Running Sum of 1d Array

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/running-sum-of-1d-array/) &nbsp;|&nbsp; **Solved:** 2025-11-27

---

## 📝 Summary

Given an array of integers, compute the running sum of the array.

## 🔍 Key Observation

The key insight is to use a running total to accumulate the sum as you iterate through the array.

## ⚙️ Algorithm

1. Initialize an output array `out` of the same length as `nums` with all elements set to 0.
2. Set the first element of `out` to the first element of `nums`.
3. For each subsequent element in `nums`, add the current element to the previous element in `out` to compute the running sum.
4. Return the `out` array.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to a single pass through the array.` | `O(1) auxiliary space since the output array is of the same length as the input array.` |

## 🏷️ Tags

`array` `running` `sum`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        out = [0] *(len(nums))
        out[0] = nums[0]
        for i in range(1,len(nums)):
            out[i] = nums[i] + out[i-1]
        return out
```

</details>
