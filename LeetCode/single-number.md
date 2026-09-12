# 🟠 single-number — Single Number

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/single-number/) &nbsp;|&nbsp; **Solved:** 2025-11-27

---

## 📝 Summary

Given an array of integers where every element appears twice except for one, find the single number.

## 🔍 Key Observation

The XOR operation has the property that a^a = 0 and a^0 = a, which allows for the elimination of duplicates.

## ⚙️ Algorithm

Iterate through the array and apply the XOR operation to each element. The result will be the single number that appears only once.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to a single pass through the array.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`bitwise` `single` `number`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0 
        for i in range(len(nums)):
            result^=nums[i]
        return result
```

</details>
