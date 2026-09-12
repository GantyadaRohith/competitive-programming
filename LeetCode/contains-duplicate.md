# 🟠 contains-duplicate — Contains Duplicate

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/contains-duplicate/) &nbsp;|&nbsp; **Solved:** 2026-05-13

---

## 📝 Summary

Given an array of integers, determine if any integer appears more than once.

## 🔍 Key Observation

Use a dictionary to track seen numbers efficiently.

## ⚙️ Algorithm

Iterate through the array, using a dictionary to store each number as you encounter it. If a number is already in the dictionary, return True. If the loop completes without finding duplicates, return False.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to a single pass through the array.` | `O(n) auxiliary space for the dictionary.` |

## 🏷️ Tags

`python` `hashmap` `dictionary` `array`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dp = {}

        for i in nums:
            if i in dp:
                return True
            dp[i] = 1
        return False
```

</details>
