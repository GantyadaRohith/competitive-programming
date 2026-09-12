# 🟠 two-sum-ii-input-array-is-sorted — Two Sum II - Input Array Is Sorted

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) &nbsp;|&nbsp; **Solved:** 2025-11-27

---

## 📝 Summary

Given a sorted array of integers and a target sum, find two numbers that add up to the target.

## 🔍 Key Observation

The array is sorted, which allows for a two-pointer technique to efficiently find the two numbers.

## ⚙️ Algorithm

1. Initialize an empty dictionary `seen` to keep track of the numbers we have seen and their indices.
2. Iterate through the array with two pointers: `i` starting at the beginning and `j` at the end.
3. Calculate the difference `diff` between the target and the current number `v`.
4. If `diff` is in `seen`, return the indices of the two numbers.
5. Otherwise, add the current number `v` and its index to `seen` and move the `j` pointer to the left.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to a single pass through the array.` | `O(n) for the `seen` dictionary.` |

## 🏷️ Tags

`two-pointer` `sorted` `array` `two-sum`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i,v in enumerate(nums):
            diff = target - v
            if diff in seen :
                return [seen[diff],i+1]
            seen[v] = i+1  
```

</details>
