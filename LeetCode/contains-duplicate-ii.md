# 🟠 contains-duplicate-ii — Contains Duplicate II

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/contains-duplicate-ii/) &nbsp;|&nbsp; **Solved:** 2026-05-13

---

## 📝 Summary

Given an array of integers and an integer k, determine if there are any two distinct indices i and j in the array such that nums[i] == nums[j] and the absolute difference between i and j is at most k.

## 🔍 Key Observation

Use a dictionary to track the last seen index of each number and check the condition for duplicates within the window of size k.

## ⚙️ Algorithm

Iterate through the array with an index i. For each number, check if it has been seen before. If it has, calculate the absolute difference between the current index i and the last seen index of the number. If this difference is less than or equal to k, return True. Otherwise, update the last seen index of the number in the dictionary. If no such pair is found, return False.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) as we iterate through the array once.` | `O(n) for the dictionary to store the last seen indices.` |

## 🏷️ Tags

`hashmap` `sliding window` `array`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dp = {}

        for i in range(len(nums)):
            if nums[i] in dp:
                if abs(dp[nums[i]]-i)<= k:
                    return True
            dp[nums[i]] = i
        return False
```

</details>
