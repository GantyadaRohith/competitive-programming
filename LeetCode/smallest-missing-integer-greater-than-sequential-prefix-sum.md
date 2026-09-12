# 🟠 smallest-missing-integer-greater-than-sequential-prefix-sum — Smallest Missing Integer Greater Than Sequential Prefix Sum

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/smallest-missing-integer-greater-than-sequential-prefix-sum/) &nbsp;|&nbsp; **Solved:** 2026-08-13

---

## 📝 Summary

Given a list of integers, find the smallest integer greater than the sum of all sequential prefixes that is not present in the list.

## 🔍 Key Observation

The key insight is to calculate the sum of sequential prefixes and then find the smallest missing integer greater than this sum.

## ⚙️ Algorithm

1. Initialize the sum `s` with the first element of the list.
2. Iterate through the list starting from the second element, updating `s` by adding the current element if it is consecutive to the previous element.
3. Break the loop if a non-consecutive element is found.
4. Use a while loop to find the smallest missing integer greater than `s` by incrementing `s` until it is not in the list.
5. Return `s` as the result.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to the single pass through the list.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`short` `lowercase` `leetcode` `prefix` `sum`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        s = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                s += nums[i]
            else:
                break

        while s in nums:
            s += 1

        return s
```

</details>
