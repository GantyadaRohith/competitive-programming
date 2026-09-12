# 🟠 find-all-numbers-disappeared-in-an-array — Find All Numbers Disappeared in an Array

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/) &nbsp;|&nbsp; **Solved:** 2025-12-03

---

## 📝 Summary

Given an array of integers where each integer is between 1 and the length of the array, find all the numbers that do not appear in the array.

## 🔍 Key Observation

The solution leverages the array itself to mark visited numbers by negating the value at the index corresponding to each number.

## ⚙️ Algorithm

1. Iterate through the array. For each number, mark the number at the index (absolute value of the number minus one) as negative if it hasn't already been marked.
2. After marking, iterate through the array again. The indices that still have positive values correspond to the numbers that are missing from the array.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to two passes through the array.` | `O(1) auxiliary space as we modify the input array in place.` |

## 🏷️ Tags

`array` `marking` `missing numbers`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        for i in range(len(nums)):
            index = abs(nums[i]) - 1  
            if nums[index] > 0:
                nums[index] *= -1  

        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)  

        return result

```

</details>
