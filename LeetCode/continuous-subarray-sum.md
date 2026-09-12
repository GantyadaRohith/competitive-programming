# 🟠 continuous-subarray-sum — Continuous Subarray Sum

![Platform](https://img.shields.io/badge/Platform-LeetCode-FFA116?style=flat-square) ![Language](https://img.shields.io/badge/Language-python-3776AB?style=flat-square)

**Problem link:** [View on LeetCode](https://leetcode.com/problems/continuous-subarray-sum/) &nbsp;|&nbsp; **Solved:** 2026-08-22

---

## 📝 Summary

Given an array of integers and a target sum, determine if there exists a continuous subarray whose sum equals the target.

## 🔍 Key Observation

The problem can be solved using a prefix sum approach with a hash map to track remainders of the prefix sums modulo the target.

## ⚙️ Algorithm

1. Initialize a list `pre` to store prefix sums and a dictionary `a` to store remainders and their indices.
2. Iterate through the array, updating the prefix sum and computing the remainder modulo the target.
3. If the remainder is zero and the index is greater than or equal to 2, return True.
4. If the remainder is already in the dictionary, check if the distance between the current index and the stored index is at least 2.
5. If no such subarray is found, return False.

## ⏱️ Complexity

| Time | Space |
|:--:|:--:|
| `O(n) due to a single pass through the array and dictionary operations.` | `O(n) for storing prefix sums and dictionary entries.` |

## 🏷️ Tags

`prefix sum` `hash map` `subarray` `sum`

<details>
<summary>💻 View solution</summary>

```python
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) == 1:
            return False
        pre = [nums[0]]
        for i in range(1,len(nums)):
            pre.append(pre[-1]+nums[i])
        a = defaultdict(list)
        for i in range(len(pre)):
            pre[i] = pre[i]%k
            if pre[i] == 0 and i>=1:
                return True
            a[pre[i]].append(i)
        f = 0
        for i,j in a.items():
            if len(j) >= 2:
                if max(j)-min(j)>=2:
                    f = 1
                    break
        return False if f == 0 else True
               
        
```

</details>
