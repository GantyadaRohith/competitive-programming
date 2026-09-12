# 🟠 majority-element — Majority Element

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/majority-element/) &nbsp;|&nbsp; **Solved:** 2026-07-13

---

## 📝 Summary

Find the element that appears more than n/2 times in an array.

## 🔍 Key Observation

Use a dictionary to count occurrences and find the majority element.

## ⚙️ Algorithm

Iterate through the array, using a dictionary to keep track of the count of each element. If the count of an element exceeds n/2, it is the majority element.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to a single pass through the array.` | `O(n) for the dictionary used to store counts.` |

## 🏷️ Tags

`hash` `counting` `dictionary`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        limit = n//2
        x = {}
        res = nums[0]
        for i in nums:
            x[i] = x.get(i,0) + 1
            if x[i] > limit:
                res = i
        return res
```

</details>
