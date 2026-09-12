# 🟠 split-array-largest-sum — Split Array Largest Sum

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/split-array-largest-sum/) &nbsp;|&nbsp; **Solved:** 2026-02-25

---

## 📝 Summary

Given an array of non-negative integers and a positive integer k, divide the array into k non-empty subarrays such that the maximum sum of any subarray is minimized.

## 🔍 Key Observation

The problem can be solved using a binary search approach to find the minimum possible maximum sum of subarrays.

## ⚙️ Algorithm

1. Define a helper function `splits` that counts the number of subarrays needed to split the array with a given maximum sum `n`.
2. Initialize `low` to the maximum value in the array and `high` to the sum of all elements in the array.
3. Perform a binary search to find the minimum possible maximum sum:
   - Calculate the middle value `mid`.
   - Use the `splits` function to count the number of subarrays needed with `mid` as the maximum sum.
   - If the number of subarrays is less than or equal to `k`, adjust the upper bound `high` to `mid-1`.
   - Otherwise, adjust the lower bound `low` to `mid+1`.
4. Return the lower bound `low` as the minimum possible maximum sum.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n log(sum(nums))) due to the binary search and the `splits` function.` | `O(1) auxiliary space.` |

## 🏷️ Tags

`binary search` `divide and conquer` `subarray` `maximum sum`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def splits(num,n):
            x = 1
            s = 0
            for i in range(len(num)):
                if s+num[i]<=n:
                    s+=num[i]
                else:
                    x+=1
                    s = num[i]
            return x
        low = max(nums)
        high = sum(nums)
        while low<= high:
            mid = low + (high-low)//2
            split = splits(nums,mid)
            if split<=k:
                high = mid-1
            else:
                low = mid+1
        return low

```

</details>
