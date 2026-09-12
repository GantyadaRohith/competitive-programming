# 🟠 subsets-ii — Subsets II

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/subsets-ii/) &nbsp;|&nbsp; **Solved:** 2026-08-22

---

## 📝 Summary

The problem asks to generate all unique subsets (power set) from an integer array that may contain duplicate elements.

## 🔍 Key Observation

To handle duplicate numbers and ensure unique subsets, sort the input array first. During backtracking, skip selecting an element if it is identical to the previous element considered at the same recursion level, and it's not the first element chosen at that level.

## ⚙️ Algorithm

**Backtracking**

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(N * 2^N)` | `O(N)` |

## 🏷️ Tags

`backtracking` `recursion` `subsets` `array` `duplicates`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def backtrack(start, curr):
            res.append(curr[:])

            for i in range(start, len(nums)):

                if i > start and nums[i] == nums[i - 1]:
                    continue

                curr.append(nums[i])
                backtrack(i + 1, curr)
                curr.pop()

        backtrack(0, [])

        return res
```

</details>
