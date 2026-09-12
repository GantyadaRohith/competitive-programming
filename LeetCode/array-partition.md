# 🟠 array-partition — Array Partition

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/array-partition/) &nbsp;|&nbsp; **Solved:** 2025-11-20

---

## 📝 Summary

Given an array of integers, find the sum of the minimum values of each pair of adjacent elements.

## 🔍 Key Observation

Sorting the array allows pairs to be easily compared and summed.

## ⚙️ Algorithm

1. Sort the array to bring adjacent elements next to each other.
2. Iterate through the sorted array in steps of 2.
3. For each pair of adjacent elements, add the smaller of the two to a running sum.
4. Return the total sum.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log n) due to sorting.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`sort` `pair` `sum`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        arr = []
        for i in range(0,len(nums),2):
            arr.append((nums[i],nums[i+1]))
        sum = 0
        for i in range(len(arr)):
            sum+=min(arr[i][0],arr[i][1])
        return sum
```

</details>
