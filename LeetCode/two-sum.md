# 🟠 two-sum — Two Sum

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/two-sum/) &nbsp;|&nbsp; **Solved:** 2026-07-01

---

## 📝 Summary

Given an array of integers and a target integer, find two numbers in the array that add up to the target.

## 🔍 Key Observation

Use a hash map to store numbers and their indices for quick lookup.

## ⚙️ Algorithm

Iterate through the array, for each number calculate its complement with respect to the target. Check if the complement exists in the hash map. If it does, return the indices of the two numbers. If not, add the current number and its index to the hash map.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to a single pass through the array and hash map operations.` | `O(n) for the hash map storing the numbers and their indices.` |

## 🏷️ Tags

`hashmap` `two-sum`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def twoSum(self,nums, target):
        mp = {}
    
        for i, num in enumerate(nums):
            complement = target - num
    
            if complement in mp:
                return [mp[complement], i]
    
            mp[num] = i
```

</details>
