# 🟠 permutations — Permutations

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/permutations/) &nbsp;|&nbsp; **Solved:** 2026-07-11

---

## 📝 Summary

Generate all possible permutations of a given list of numbers.

## 🔍 Key Observation

Use a recursive backtracking approach to explore all permutations.

## ⚙️ Algorithm

1. Initialize an empty list `res` to store permutations and an empty list `seen` to keep track of the current permutation being built.
2. Define a recursive function `perm` that takes the list `nums` and the current `seen` permutation.
3. If the length of `seen` equals the length of `nums`, append a copy of `seen` to `res` and return.
4. For each number in `nums`, if it is not in `seen`, add it to `seen`, call `perm` recursively, and then remove it from `seen` to backtrack.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n!) due to the factorial number of permutations.` | `O(n) auxiliary space due to the recursion stack and `seen` list.` |

## 🏷️ Tags

`backtracking` `permutations`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def perm(nums,seen):
            if len(seen) == len(nums):
                res.append(seen[:])
                return
            for i in nums:
                if i not in seen:
                    seen.append(i)
                    perm(nums,seen)
                    seen.pop()
        perm(nums,[])
        return res
```

</details>
