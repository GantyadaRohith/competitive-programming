# 🟠 maximum-valid-pair-sum — Maximum Valid Pair Sum

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/maximum-valid-pair-sum/) &nbsp;|&nbsp; **Solved:** 2026-07-18

---

## 📝 Summary

Given an array of integers and a target sum, find the maximum sum of any pair of numbers in the array that equals the target sum.

## 🔍 Key Observation

The key insight is to use a prefix array to store the maximum value encountered so far up to each index, allowing for efficient lookup of the complement of the current number to reach the target sum.

## ⚙️ Algorithm

1. Initialize a prefix array `pre` where `pre[i]` contains the maximum value in the array up to index `i`. This helps in quickly finding the complement of the current number to reach the target sum `k` by checking `pre[i-k]` if `i >= k`. 2. Iterate through the array, updating the prefix array and checking for the maximum sum of pairs that sum up to `k`. 3. Return the maximum sum found.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to a single pass through the array to build the prefix array and another pass to find the maximum sum.` | `O(n) for the prefix array.` |

## 🏷️ Tags

`python` `prefix` `array` `two-pointer`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def maxValidPairSum(self, nums: list[int], k: int) -> int:
        n = len(nums)
        maxi = 0
        pre = [-1]*(n)
        pre[0] = nums[0]
        print(pre)
        for i in range(1,n):
            pre[i] = max(pre[i-1],nums[i])
        for i in range(k,n):
            maxi = max(maxi,nums[i]+pre[i-k])
        return maxi

```

</details>
