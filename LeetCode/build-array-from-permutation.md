# 🟠 build-array-from-permutation — Build Array from Permutation

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/build-array-from-permutation/) &nbsp;|&nbsp; **Solved:** 2025-11-27

---

## 📝 Summary

Constructs a new array where each element at index i is the value at index nums[i] in the original array.

## 🔍 Key Observation

The solution uses a single pass through the input array to construct the output array efficiently.

## ⚙️ Algorithm

The algorithm iterates over the input array `nums`. For each element at index `i`, it places the value at index `nums[i]` in the output array `ans` at index `i`. This is done by updating `ans[j]` to `nums[i]` and then incrementing `j` by 1. This approach ensures that the output array is constructed in a single pass, achieving O(n) time complexity.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to a single pass through the input array.` | `O(1) auxiliary space as the output array `ans` is created in place.` |

## 🏷️ Tags

`python` `array` `single pass`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = [0]*(len(nums))
        j = 0 
        for i in nums:
            ans[j] = nums[i]
            j+=1
        return ans
```

</details>
