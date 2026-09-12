# 🟠 find-missing-elements — Find Missing Elements

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/find-missing-elements/) &nbsp;|&nbsp; **Solved:** 2026-08-04

---

## 📝 Summary

Given an array of integers where one number is missing, find all the missing numbers in the range [1, n].

## 🔍 Key Observation

The solution leverages the properties of the range and the presence of numbers in the array to identify missing elements.

## ⚙️ Algorithm

1. Determine the minimum and maximum values in the array to define the range [mi, ma].
2. Iterate through the range from mi to ma.
3. For each number in the range, check if it is present in the array.
4. If a number is not found in the array, it is a missing element.
5. Collect all missing elements in a list and return it.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to the single pass through the range and the single pass through the array.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`easy` `array` `missing` `elements`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        mi,ma=min(nums),max(nums)
        out = []
        for i in range(mi,ma+1):
            if i not in nums:
                out.append(i)
        return out
            
```

</details>
