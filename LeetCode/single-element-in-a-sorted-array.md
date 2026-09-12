# 🟠 single-element-in-a-sorted-array — Single Element in a Sorted Array

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/single-element-in-a-sorted-array/) &nbsp;|&nbsp; **Solved:** 2026-07-13

---

## 📝 Summary

Given a sorted array with all elements except one appearing twice, find the single element.

## 🔍 Key Observation

The XOR operation can be used to find the single element because it cancels out pairs of identical numbers.

## ⚙️ Algorithm

Iterate through the array and apply the XOR operation to each element. The result will be the single element, as all other elements will cancel out.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to a single pass through the array.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`xor` `single` `element` `sorted`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        x = 0
        for i in nums:
            x = x^i
        return x
```

</details>
