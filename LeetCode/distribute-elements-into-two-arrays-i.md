# 🟠 distribute-elements-into-two-arrays-i — Distribute Elements Into Two Arrays I

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/distribute-elements-into-two-arrays-i/) &nbsp;|&nbsp; **Solved:** 2026-08-21

---

## 📝 Summary

Given an array of integers, distribute the elements into two arrays such that the sum of the first array is greater than or equal to the sum of the second array.

## 🔍 Key Observation

The key insight is to maintain the sum of the first array greater than or equal to the sum of the second array by comparing the last elements of both arrays.

## ⚙️ Algorithm

1. Initialize two arrays, `arr1` and `arr2`, with the first two elements of the input array `nums` respectively.
2. Iterate through the remaining elements of `nums` starting from the third element.
3. For each element, compare the last elements of `arr1` and `arr2`:
   - If the last element of `arr1` is greater than or equal to the last element of `arr2`, append the current element to `arr1`.
   - Otherwise, append the current element to `arr2`.
4. Return the concatenation of `arr1` and `arr2`.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to a single pass through the input array.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`array` `two-pointer` `greedy`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = [nums[0]]
        arr2 = [nums[1]]
        for i in range(2,len(nums)):
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])
        return arr1+arr2
```

</details>
