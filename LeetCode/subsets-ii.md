# 🟠 subsets-ii — Subsets II

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/subsets-ii/) &nbsp;|&nbsp; **Solved:** 2026-08-22

---

## 📝 Summary

Given a collection of integers that may contain duplicates, return all unique subsets.

## 🔍 Key Observation

Sorting the input array helps in handling duplicates and simplifies the backtracking process.

## ⚙️ Algorithm

The solution uses backtracking to explore all possible subsets. It first sorts the array to ensure that duplicates are adjacent. The `backtrack` function builds subsets by adding elements to the current subset and recursively exploring further. It skips duplicate elements to avoid duplicate subsets in the result.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n * 2^n) due to the generation of all subsets and the backtracking process.` | `O(n * 2^n) for storing all subsets and the recursion stack.` |

## 🏷️ Tags

`backtracking` `subset` `duplicate`

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
