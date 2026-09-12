# 🟠 move-zeroes — Move Zeroes

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/move-zeroes/) &nbsp;|&nbsp; **Solved:** 2026-07-02

---

## 📝 Summary

Given an array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

## 🔍 Key Observation

The key insight is to use a single pass to identify and swap non-zero elements to the front of the array.

## ⚙️ Algorithm

1. Initialize a pointer `j` to -1. This pointer will mark the position where the next non-zero element should be placed.
2. Iterate through the array with index `i`:
   - If `nums[i]` is 0, update `j` to `i` if it's the first zero encountered.
   - If `nums[i]` is non-zero and `j` is not -1, swap `nums[i]` with `nums[j]` and increment `j`.
3. The array is now rearranged with all non-zero elements to the front, and zeros are moved to the end.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to a single pass through the array.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`array` `two-pointer` `move-zeroes`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                j = i
                break
        if j == -1:
            return
        for i in range(j + 1, len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1



```

</details>
