# 🟠 subsets — Subsets

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/subsets/) &nbsp;|&nbsp; **Solved:** 2026-07-11

---

## 📝 Summary

Given a set of integers, generate all possible subsets of the set.

## 🔍 Key Observation

Backtracking is a powerful technique for generating all combinations of a set.

## ⚙️ Algorithm

The solution uses a recursive backtracking approach. It iterates through each element in the input list, adding it to the current subset and then recursively exploring further. After exploring, it removes the last element to backtrack and try the next option. This process continues until all subsets are generated.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(2^n) due to generating all subsets.` | `O(n) auxiliary space for the recursion stack.` |

## 🏷️ Tags

`backtracking` `generate` `combinations`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [];curr = []

        def backtrack(i):
            if i == len(nums):
                res.append(curr[:])
                return

            curr.append(nums[i])
            backtrack(i+1)

            curr.pop()
            backtrack(i+1)

        backtrack(0)
        return res
```

</details>
