# 🟠 predict-the-winner — Predict the Winner

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/predict-the-winner/) &nbsp;|&nbsp; **Solved:** 2026-08-02

---

## 📝 Summary

Given a list of integers, determine if the first player can win the game of Nim by choosing the optimal strategy.

## 🔍 Key Observation

The problem can be solved using dynamic programming to find the optimal strategy for the first player.

## ⚙️ Algorithm

The solution uses a recursive function `solve` with memoization to determine the maximum difference in scores between the two players for any subarray. The base case is when the subarray is empty, returning 0. The function calculates the maximum score difference by considering two choices: picking the first element or the last element of the subarray, and recursively solving the remaining subarrays. The memoization ensures that each subproblem is solved only once, improving efficiency.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n^2) due to the nested loops and memoization.` | `O(n^2) for the memoization table.` |

## 🏷️ Tags

`dp` `memoization` `nim` `game theory`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        memo = {}
        def solve(l, r):
            if l > r:
                return 0
            if memo.get((l,r),0):
                return memo[(l,r)]
            left = nums[l] - solve(l + 1, r)
            right = nums[r] - solve(l, r - 1)
            memo[(l,r)] = max(left,right)
            return memo[(l,r)]
            
        a = solve(0,len(nums)-1) 
        if a>=0:
            return True
        else:
            return False 
```

</details>
