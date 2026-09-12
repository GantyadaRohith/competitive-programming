# 🟠 unique-binary-search-trees — Unique Binary Search Trees

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/unique-binary-search-trees/) &nbsp;|&nbsp; **Solved:** 2026-03-06

---

## 📝 Summary

Given a positive integer n, find the number of unique binary search trees (BSTs) that can be constructed with n distinct nodes.

## 🔍 Key Observation

The number of unique BSTs with n nodes is given by the nth Catalan number.

## ⚙️ Algorithm

The solution uses dynamic programming to calculate the number of BSTs. It initializes a DP array where dp[i] represents the number of unique BSTs with i nodes. For each i, it calculates the number of BSTs by considering all possible root nodes and summing up the products of the number of left and right subtrees.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n^2) due to the nested loops.` | `O(n) auxiliary space for the DP array.` |

## 🏷️ Tags

`dp` `catalan` `binary search trees`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def numTrees(self, n: int) -> int:
        if n<=1:
            return 1
        dp = [0]*(n+1)
        dp[0] = 1
        for i in range(1,n+1):
            temp = (2*(2*i-1))/(i+1)
            dp[i] = dp[i-1]*temp
        return (int(dp[-1]))
```

</details>
