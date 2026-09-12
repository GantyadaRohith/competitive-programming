# 🟠 find-all-duplicates-in-an-array — Find All Duplicates in an Array

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/find-all-duplicates-in-an-array/) &nbsp;|&nbsp; **Solved:** 2025-12-03

---

## 📝 Summary

Given an array of integers, find all numbers that appear more than once.

## 🔍 Key Observation

Using the array itself as a hash table to track seen numbers.

## ⚙️ Algorithm

Iterate through the array. For each number, mark the corresponding index as negative. If the index is already negative, it means the number has been seen before, so add it to the result list.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to a single pass through the array.` | `O(1) auxiliary space, as we only use a constant amount of extra space.` |

## 🏷️ Tags

`array` `hash` `in-place`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        a = []
        for num in nums:
            if nums[abs(num)-1] < 0:
                a.append(abs(num))
            else:
                nums[abs(num)-1] *= -1
        return a
```

</details>
